import logging

from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.simple import direct_to_template


logger = logging.getLogger(__name__)
from .models import Lesson



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
