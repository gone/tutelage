from django.conf.urls.defaults import *
from .views import LessonWizard, FORMS


urlpatterns = patterns('app.views',
    url(r'^lessons/$', 'lessons', name="lessons"),
    url(r'^mylessons/(?P<user_id>\d+)/$', 'mylessons', name="mylessons"),
    url(r'^profile/(?P<user_id>\d+)/$', 'profile', name="profile"),
    url(r'^profile/$', 'profile', name="self_profile"),
    url(r'^miniprofile/(?P<user_id>\d+)/$', 'miniprofile', name="miniprofile"),
    url(r'^chief-list/$', "cheiflist", name="chieflist"),
    url(r'^add-lesson/$', "add_lesson", name="add-lesson" ),
    url(r'^add-lesson/(?P<lesson_id>\d+/)/$', "edit_lesson", name="edit-lesson" ),
    url(r'^add-lesson/(?P<lesson_id>\d+/)/ingreidents/$', "lesson_ingredients", name="lesson_ingredients" ),
    url(r'^add-lesson/(?P<lesson_id>\d+/)/steps$', "lesson_steps", name="lesson_steps" ),

)
