import logging
import json

from django.shortcuts import get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.simple import direct_to_template
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.validators import ValidationError
from django.views.decorators.http import require_POST


from django.forms.models import inlineformset_factory, modelformset_factory


from django.core.exceptions import PermissionDenied


logger = logging.getLogger(__name__)

from .models import Lesson, LessonIngredient, Tool, Step, Video, LessonRating
from .forms import ProfileForm, LessonDetailsForm, IngredentsDetailsForm, StepDetailsForm

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
        user = get_object_or_404(User, pk=user_id)
        return direct_to_template(request, "profile.html", {"u":user})

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
    return direct_to_template(request, "lessondetails.html", {"lesson": lesson})


def mylessons(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    all_lessons = user.teaching.all()
    lesson_paginator = Paginator(all_lessons, 16)
    lesson_page = request.GET.get('lessons')
    try:
        lessons = lesson_paginator.page(lesson_page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        lessons = lesson_paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        lessons = lesson_paginator.page(lesson_paginator.num_pages)

    return direct_to_template(request, "mylessons.html", {"lessons": lessons, "u":user})



TEMPLATES = {'lesson_details': "lesson_details_form.html",
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
    return direct_to_template(request, "lesson_details_form.html",
                              {"form": form, "lesson_id": lesson_id})


@csrf_exempt
def add_lesson_video(request):
    data = request.POST[settings.TRANSLOADIT_DATAFIELD]
    data = json.loads(data)
    lesson = get_object_or_404(Lesson, pk=data['fields']['lesson_id'])

    # TODO: move to other module, and use settings to use
    response_ok = HttpResponse('OK')
    code = data.get('error', False)
    if code:
        # TODO: handle error
        return response_ok

    # XXX: ignores more than one uploads
    # Only accepting one video at a time
    # may be later accept more
    uploads = data['uploads']
    if len(uploads) > 1:
        return response_ok

    # create Video
    duration = uploads[0]['meta']['duration']
    results = data['results']
    # ignore the original video
    results.pop(':original', None)
    for r in results.values():
        r = r[0]
        m = r['meta']
        Video.objects.create(
            lesson=lesson,
            remote_id=r['id'],
            original_id=r['original_id'],
            mime=r['mime'],
            size=r['size'],
            url=r['url'],
            ext=r['ext'],
            name=r['name'],
            duration=duration,
            width=m['width'],
            height=m['height'],
            video_codec=m['video_codec'],
            audio_codec=m['audio_codec'],
        )
    return response_ok


@login_required
def lesson_ingredients(request, lesson_id=None):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.user != lesson.teacher:
        raise PermissionDenied

    IngredientsDetailsFormset = inlineformset_factory(Lesson, LessonIngredient, form=IngredentsDetailsForm, extra=1, )
    ToolFormset = modelformset_factory(Tool, extra=1)
    if request.method == "POST":
        ingredient_formset = IngredientsDetailsFormset(request.POST, instance=lesson, prefix="ingredients")
        tool_formset = ToolFormset(request.POST, prefix="tools", queryset=lesson.tools.all())
        if ingredient_formset.is_valid() and tool_formset.is_valid():
            # XXX: unused Ingredients
            ingredients = ingredient_formset.save()
            tools = tool_formset.save()
            for tool in tools:
                lesson.tools.add(tool)
        return HttpResponseRedirect(reverse("lesson_steps",
                                            kwargs={'lesson_id': lesson.id}))
    else:
        ingredient_formset = IngredientsDetailsFormset(instance=lesson, prefix="ingredients")
        tool_formset = ToolFormset(prefix="tools", queryset=lesson.tools.all())
    return direct_to_template(request, "ingredients_details_form.html",
                              {"ingredient_formset": ingredient_formset,
                               "tool_formset": tool_formset,
                               "lesson": lesson,
                               })

@login_required
def lesson_steps(request, lesson_id=None):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.user != lesson.teacher:
        raise PermissionDenied

    StepFormset = inlineformset_factory(Lesson, Step, extra=1)
    if request.method == "POST":
        step_formset = StepFormset(request.POST, queryset=lesson.steps.all(), instance=lesson)
        if step_formset.is_valid():
            steps = step_formset.save()
            for step in steps:
                lesson.steps.add(step)
            return HttpResponseRedirect(reverse("self_profile"))
    else:
        step_formset = StepFormset(queryset=lesson.steps.all(), instance=lesson)

    return direct_to_template(request, "step_details_form.html", {"form": step_formset, "lesson": lesson,})


def cheflist(request):
    pass


def lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    steps = list(lesson.steps.all())
    for idx, step in enumerate(steps):
        if idx+1 == len(steps):
            continue
        step.end_time = steps[idx+1].start_time
    lesson.s = steps
    return direct_to_template(request, "lesson.html", {"lesson": lesson})

@csrf_exempt
@require_POST
@login_required
def rate_lesson(request, lesson_id, rating):
    r, created = LessonRating.objects.get_or_create(user=request.user, lesson_id=lesson_id, defaults={rating:rating})
    if not created:
        r.rating = rating
        r.save()
    return HttpResponse('OK')
