import json
import logging
from itertools import chain

from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.simple import direct_to_template
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.validators import ValidationError
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.core import serializers

from django.forms.models import inlineformset_factory, modelformset_factory


from django.core.exceptions import PermissionDenied

from django.contrib.formtools.wizard.views import SessionWizardView


logger = logging.getLogger(__name__)

from .models import (Lesson, LessonIngredient, Tool, Step, Video,
                     LessonRating, FeaturedChef, LessonRequest)

from .forms import (ProfileForm,
                    LessonDetailsForm,
                    IngredentsDetailsForm,
                    ToolsDetailsForm,
                    StepDetailsForm,
                    ChefPledgeForm,
                    ContributionForm,
                    LessonRequestForm)

from account.forms import PasswordChangeForm

from django.contrib.auth.models import User


def profile(request, user_id=None):
    if request.user.is_authenticated() and user_id in [None, str(request.user.id)]:
        profile = request.user.get_profile()

        if request.method == "POST":
            form = ProfileForm(request.POST, profile=profile)
            if form.is_valid():
                profile = form.save()
                form = ProfileForm(profile=profile)
        else:
            form = ProfileForm(profile=profile)
        cpass_form = PasswordChangeForm(request.user)
        return direct_to_template(request, "profile.html", {"u":request.user, "form": form, "cpass_form":cpass_form})
    elif request.user.is_anonymous() and user_id is None:
        return HttpResponseRedirect(reverse("account:auth_login"))
    else:
        user = get_object_or_404(User, pk=user_id, profile__professional_chef=True)
        return direct_to_template(request, "chef_profile.html", {"u":user})

def miniprofile(request, user_id):
    """The mini profile for user profile's in light boxes"""
    user = get_object_or_404(User, pk=user_id)
    return direct_to_template(request, "wprofile.html", {"u":user})

def lessons(request):
    all_lessons = Lesson.objects.all()
    paginator = Paginator(all_lessons, 16)
    page = request.GET.get('page')
    try:
        lessons = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        lessons = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        lessons = paginator.page(paginator.num_pages)

    return direct_to_template(request, "lessons.html", {"lessons": lessons})

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return direct_to_template(request, "lesson_details.html", {"lesson": lesson})


def mylessons(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    all_lessons = user.lessons.all()
    lesson_paginator = Paginator(all_lessons, 16)
    lesson_page = request.GET.get('page')
    try:
        lessons = lesson_paginator.page(lesson_page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        lessons = lesson_paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        lessons = lesson_paginator.page(lesson_paginator.num_pages)

    return direct_to_template(request, "mylessons.html", {"lessons": lessons, "u":user})



TEMPLATES = { 'lesson_details': "lesson_details_form.html",
              'ingredents_details': "ingredents_details_form.html",
              'step_details': "step_details_form.html",
              }

@login_required
def add_lesson(request, lesson_id=None):
    if lesson_id:
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        if  request.user != lesson.teacher:
            raise PermissionDenied
    else:
        lesson = None
    if request.method == "POST":
        form = LessonDetailsForm(request.POST, request.FILES, instance=lesson)
        if form.is_valid():
            lesson = form.save(False)
            lesson.teacher = request.user
            lesson.save()
            return redirect("lesson_ingredients", lesson_id=lesson.id)
    else:
        form = LessonDetailsForm(instance=lesson)
    return direct_to_template(request, "lesson_details_form.html", {"form": form, "lesson_id":lesson_id})


@login_required
def add_lesson_video(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    video = Video(video=request.FILES['video'], lesson=lesson)
    try:
        video.clean()
    except ValidationError, e:
        return HttpResponse(str(e), status=400)
    video.save()
    return HttpResponse('OK')


@login_required
def lesson_ingredients(request, lesson_id=None):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.user != lesson.teacher:
        raise PermissionDenied

    IngredientsDetailsFormset = inlineformset_factory(Lesson, LessonIngredient, form=IngredentsDetailsForm, extra=1, )
    ToolFormset = modelformset_factory(Tool, extra=1, form=ToolsDetailsForm)
    if request.method == "POST":
        ingredient_formset = IngredientsDetailsFormset(request.POST, instance=lesson, prefix="ingredients")
        tool_formset = ToolFormset(request.POST, prefix="tools", queryset=lesson.tools.all())
        if ingredient_formset.is_valid() and tool_formset.is_valid():
            ingredients = ingredient_formset.save()
            tools = tool_formset.save()
            for tool in tools:
                lesson.tools.add(tool)
        if lesson.kind == 1:
            return HttpResponseRedirect(reverse("lesson_video",  kwargs={'lesson_id':lesson.id}))
        else:
            return HttpResponseRedirect(reverse("lesson_steps",  kwargs={'lesson_id':lesson.id}))
    else:
        ingredient_formset = IngredientsDetailsFormset(instance=lesson, prefix="ingredients")
        tool_formset = ToolFormset(prefix="tools", queryset=lesson.tools.all())
    return direct_to_template(request, "ingredients_details_form.html",
                              {"ingredient_formset": ingredient_formset,
                               "tool_formset": tool_formset,
                               "lesson": lesson,
                               })
@login_required
def lesson_video(request, lesson_id=None):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.user != lesson.teacher:
        raise PermissionDenied

    return direct_to_template(request, "video_details_form.html", {"lesson": lesson,})

@login_required
def lesson_steps(request, lesson_id=None):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.user != lesson.teacher:
        raise PermissionDenied

    StepFormset = inlineformset_factory(Lesson, Step, extra=1, form=StepDetailsForm)
    if request.method == "POST":
        step_formset = StepFormset(request.POST, request.FILES, queryset=lesson.steps.all(), instance=lesson, initial=[{'lesson': lesson}])



        if step_formset.is_valid():
            steps = step_formset.save()
            for step in steps:
                lesson.steps.add(step)
            return HttpResponseRedirect(reverse("mylessons", args=[request.user.id]))
    else:
        step_formset = StepFormset(queryset=lesson.steps.all(), instance=lesson, initial=[{'lesson': lesson}])
    return direct_to_template(request, "step_details_form.html", {"form": step_formset, "lesson": lesson,})

@login_required
def purchase(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    lesson.followers.add(request.user)
    return HttpResponseRedirect(reverse("lesson", kwargs={'lesson_id':lesson.id}))

def cheflist(request):
    pass

@login_required
def chef_pledge(request, slug):
    lesson_request = get_object_or_404(LessonRequest, slug=slug, active=True)
    if request.method == "POST":
        form = ChefPledgeForm(request.user, lesson_request, request.POST)
        if form.is_valid():
            pledge = form.save()
            return HttpResponseRedirect("%s?slug=%s" % (reverse('ask'), lesson_request.slug))
    else:
        form = ChefPledgeForm(request.user, lesson_request)
    return direct_to_template(request, "chef_pledge_standalone.html", {"pledge_form": form, "slug":slug})

@login_required
def contribute(request):
    if request.method == "POST":
        form = ContributionForm(request.user, request.POST)
        if form.is_valid():
            contribution = form.save()
            return HttpResponseRedirect("%s?slug=%s" % (reverse('ask'), contribution.request.slug))
    else:
        form = ContributionForm(request.user)
    return direct_to_template(request, "contribute_standalone.html", {"contribute_form": form})

@login_required
def ask_form(request):
    if request.method == "POST":
        form = LessonRequestForm(request, request.POST)
        if form.is_valid():
            lesson_request = form.save()
            return HttpResponseRedirect("%s?slug=%s" % (reverse('ask'), lesson_request.slug))
    else:
        form = LessonRequestForm(request)
    return direct_to_template(request, "lesson_request_standalone.html", {"request_form": form})


def ask(request):
    all_lesson_requests = LessonRequest.objects.filter(active=True)

    per_page = 6
    req_paginator = Paginator(all_lesson_requests, per_page)

    slug = request.GET.get('slug')
    if slug:
        lesson_request = get_object_or_404(LessonRequest, slug=slug, active=True)
        count = LessonRequest.objects.filter(active=True, need_by__lte=lesson_request.need_by, id__lt=lesson_request.id).count()
        req_page = max(count / per_page, 1)
    else:
        req_page = request.GET.get('page')

    try:
        lesson_requests = req_paginator.page(req_page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        lesson_requests = req_paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        lesson_requests = req_paginator.page(req_paginator.num_pages)

    lesson_json = json.dumps({x.slug:x.to_dict() for x in lesson_requests.object_list})

    request_form = LessonRequestForm(request)
    pledge_form = ChefPledgeForm(request.user)
    contribute_form = ContributionForm(request.user)

    if not slug:
        slug = lesson_requests.object_list[0].slug

    return direct_to_template(request, "ask.html", {"contribute_form":contribute_form, "lesson_requests": lesson_requests, 'slug': slug, 'lesson_json':lesson_json, 'pledge_form':pledge_form, 'request_form':request_form})


def lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return direct_to_template(request, "lesson.html", {"lesson": lesson})

@csrf_exempt
@require_POST
@login_required
def rate_lesson(request, lesson_id, rating):
    r, created = LessonRating.objects.get_or_create(user=request.user, lesson_id=int(lesson_id), defaults={"rating":int(rating)})
    if not created:
        r.rating = rating
        r.save()
    return HttpResponse('OK')


def featured_chefs(request):
    chef = FeaturedChef.objects.published().order_by('-id').select_related('chef')[0]
    return profile(request, user_id=chef.id)
