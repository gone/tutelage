import logging

from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.simple import direct_to_template
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from django.core.exceptions import PermissionDenied

from django.contrib.formtools.wizard.views import SessionWizardView


logger = logging.getLogger(__name__)
from .models import Lesson
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



TEMPLATES = { 'lesson_details': "lesson_details_form.html",
              'ingredents_details': "ingredents_details_form.html",
              'step_details': "step_details_form.html",
              }

@login_required
def add_lesson(request, lesson_id=None):
    if lesson_id:
        instance = get_object_or_404(Lesson, pk=lesson_id)
        if  request.user != instance.teacher:
            raise PermissionDeined
    else:
        instance = None
    if request.method == "POST":
        form = LessonDetailsForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            lesson = form.save()
            return HttpRedirect(reverse("lesson_ingredients", args=[lesson.id]))
    else:
        form = LessonDetailsForm(instance=instance)
    return direct_to_template(request, "lesson_details_form.html", {"form": form})


@login_required
def lesson_ingredients(request, lesson_id):
    return direct_to_template(request, "ingredients_details_form.html")#, {"form": form})

@login_required
def lesson_steps(request, lesson_id):
    return direct_to_template(request, "step_details_form.html")#, {"form": form})


def cheflist(request):
    pass
