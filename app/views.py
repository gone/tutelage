import logging

from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.simple import direct_to_template
from django.http import Http404

logger = logging.getLogger(__name__)
from .models import Lesson
from .forms import ProfileForm

from django.contrib.auth.models import User



def profile(request, user_id=None):
    if request.user.is_authenticated() and user_id in [None, request.user.id]:
        profile = request.user.get_profile()

        if request.method == "POST":
            form = ProfileForm(request.post, profile=profile)
            if form.is_valid():
                profile = form.save()
                form = ProfileForm(profile=profile)

        return direct_to_template(request, "myprofile.html", {"user":request.user, "form": form})
    else:
        user = get_object_or_404(User, pk=user_id)
        return direct_to_template(request, "profile.html", {"user":user})


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



def mylessons(request):
    all_lessons = Lesson.objects.all()
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

    return direct_to_template(request, "mylessons.html", {"lessons": lessons})
