import json
import logging
from itertools import chain
from functools import wraps
from datetime import datetime, timedelta
from datetime import datetime
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
from django.db import transaction
from django.core.mail import EmailMessage


from django.forms.models import inlineformset_factory, modelformset_factory


from django.core.exceptions import PermissionDenied

from django.contrib.formtools.wizard.views import SessionWizardView


logger = logging.getLogger(__name__)

from .models import (Lesson, LessonIngredient, LessonTool, Step, #Video,
                     LessonRating, FeaturedChef, LessonRequest, Customer, Profile)

from .forms import (ProfileForm,
                    LessonDetailsForm,
                    IngredentsDetailsForm,
                    ToolsDetailsForm,
                    StepDetailsForm,
                    ChefPledgeForm,
                    ContributionForm,
                    LessonRequestForm,
                    LessonPurchaseForm)

from .internal_stripe import create_customer, bill_pledge

from account.forms import PasswordChangeForm

from django.contrib.auth.models import User

@transaction.commit_manually
def handle_customer_data(request):
    if request.method == "POST" and 'stripe-data' in request.POST:
        stripe_data = json.loads(request.POST['stripe-data'])
        customer = create_customer(request.user, stripe_data['id'])
        Customer.objects.create(customer_id=customer.id, user=request.user)
        transaction.commit()

def create_stripe_customer(func):

    @wraps(func)
    def wrapper(request, *args, **kwargs):
        handle_customer_data(request)
        return func(request, *args, **kwargs)
    return wrapper


@login_required(redirect_field_name='')
def profile(request, user_id=None):
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
        return direct_to_template(request, "profile.html", {"lessons": lessons, "u":user, "form": form, "cpass_form":cpass_form})
    elif request.user.is_anonymous() and user_id is None:
        return HttpResponseRedirect(reverse("account:auth_login"))
    else:
        user = get_object_or_404(User, pk=user_id, profile__professional_chef=True)
        return direct_to_template(request, "chef_profile.html", {"lessons": lessons, "u":user})

@login_required(redirect_field_name='')
def miniprofile(request, user_id):
    """The mini profile for user profile's in light boxes"""
    user = get_object_or_404(User, pk=user_id)
    return direct_to_template(request, "wprofile.html", {"u":user})

@login_required(redirect_field_name='')
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

@login_required(redirect_field_name='')
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return direct_to_template(request, "lesson_details.html", {"lesson": lesson})

def welcome(request):
    if request.method == 'POST':
            signup_email = request.POST.get('splash-signup-email')
            email_subject = "New Signup Request - " + signup_email + " wants to join Culination"
            email_body = "Another Culinator would like to join the potluck! Let " + signup_email + " know when they can sign up on Culination."
            email_message = EmailMessage(email_subject, email_body, to=['geoffrey@tutelageinc.com'])
            email_message.send(fail_silently = False)
            #request.user.message_set.create(message = "Email confirmation sent!")
            #return HttpResponseRedirect(reverse("welcome",  kwargs={'signup_email':signup_email}))
            return direct_to_template(request, "welcome.html", {'signup_email':signup_email})
    if request.user.is_authenticated():
        return redirect('/home/')
    else:
        return direct_to_template(request, "welcome.html")

TEMPLATES = { 'lesson_details': "lesson_details_form.html",
              'ingredents_details': "ingredents_details_form.html",
              'step_details': "step_details_form.html",
              }

@login_required(redirect_field_name='')
def add_lesson(request, lesson_id=None):
    if lesson_id:
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        if  request.user != lesson.teacher:
            raise PermissionDenied
    else:
        lesson = None
    if request.method == "POST":
        form = LessonDetailsForm(request.POST, request.FILES, teacher=request.user, instance=lesson)
        if form.is_valid():
            lesson = form.save(False)
            return redirect("lesson_ingredients", lesson_id=lesson.id)
    else:
        form = LessonDetailsForm(teacher=request.user, instance=lesson)
    return direct_to_template(request, "lesson_details_form.html", {"form": form, "lesson_id":lesson_id})


# @login_required
# def add_lesson_video(request, lesson_id):
#     lesson = get_object_or_404(Lesson, pk=lesson_id)
#     video = Video(video=request.FILES['video'], lesson=lesson)
#     try:
#         video.clean()
#     except ValidationError, e:
#         return HttpResponse(str(e), status=400)
#     video.save()
#     return HttpResponse('OK')


@login_required
def lesson_ingredients(request, lesson_id=None):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.user != lesson.teacher:
        raise PermissionDenied

    IngredientsDetailsFormset = inlineformset_factory(Lesson, LessonIngredient, form=IngredentsDetailsForm, extra=1, )
    ToolFormset = inlineformset_factory(Lesson, LessonTool, form=ToolsDetailsForm, extra=1, )
    if request.method == "POST":
        ingredient_formset = IngredientsDetailsFormset(request.POST, instance=lesson, prefix="ingredients")
        tool_formset = ToolFormset(request.POST, instance=lesson, prefix="tools")
        if ingredient_formset.is_valid() and tool_formset.is_valid():
            ingredients = ingredient_formset.save()
            tools = tool_formset.save()
        if lesson.kind == 1:
            return HttpResponseRedirect(reverse("lesson_video",  kwargs={'lesson_id':lesson.id}))
        else:
            return HttpResponseRedirect(reverse("lesson_steps",  kwargs={'lesson_id':lesson.id}))
    else:
        ingredient_formset = IngredientsDetailsFormset(instance=lesson, prefix="ingredients")
        tool_formset = ToolFormset(instance=lesson, prefix="tools")
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
            return HttpResponseRedirect(reverse("profile", args=[request.user.id]))
    else:
        step_formset = StepFormset(queryset=lesson.steps.all(), instance=lesson, initial=[{'lesson': lesson}])
    return direct_to_template(request, "step_details_form.html", {"form": step_formset, "lesson": lesson,})

@create_stripe_customer
@login_required
def purchase(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == "POST":
        form = LessonPurchaseForm(request.user, lesson, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("lesson", kwargs={'lesson_id':lesson.id}))
    else:
        form = LessonPurchaseForm(request.user, lesson, request.POST)
    return direct_to_template(request, "lesson_purchase_standalone.html", {"purchase_form": form, "lesson":lesson})


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

@create_stripe_customer
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

@create_stripe_customer
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

@login_required(redirect_field_name='')
def ask(request):
    all_lesson_requests = LessonRequest.objects.filter(active=True)
    active_requests = LessonRequest.objects.filter(active=True, need_by__gte=datetime.today())
    alert_date = datetime.now() + timedelta(days=1)

    per_page = 6
    req_paginator = Paginator(active_requests, per_page)

    slug = request.GET.get('request')
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
        try:
            slug = lesson_requests.object_list[0].slug
        except IndexError:
            slug = ""

    return direct_to_template(request, "ask.html", {"contribute_form":contribute_form, "lesson_requests": lesson_requests, 'slug': slug, 'lesson_json':lesson_json, 'pledge_form':pledge_form, 'request_form':request_form, 'alert_date':alert_date})

@login_required(redirect_field_name='')
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

@login_required
def featured_chefs(request):
    chef = FeaturedChef.objects.published().order_by('-id').select_related('chef')[0]
    return profile(request, user_id=chef.id)

@login_required
def cheflist(request):
    chefs_featured = FeaturedChef.objects.all()
    chefs_all = Profile.objects.filter(professional_chef=True)
    return direct_to_template(request, "featured_chef.html", {"chefs_featured": chefs_featured, "chefs": chefs_all})


def handle_requests():
    for r in LessonRequest.objects.filter(active=True, need_by__lt=datetime.today()):
        r.active=False
        if r.chef_attatched and r.in_pot > r.amount_needed:
            r.successfully_funded = True
            for pledge in r.pledges.all():
                try:
                    bill_pledge(pledge)
                    pledge.successfully_billed = True
                except:
                    pledge.successfully_billed = False
            pledge.save()

        else:
            r.successfully_funded = False
        r.save()
