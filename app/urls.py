from django.conf.urls.defaults import *
from .views import LessonWizard, FORMS


urlpatterns = patterns('app.views',
    url(r'^lessons/$', 'lessons', name="lessons"),
    url(r'^mylessons/(?P<user_id>\d+)/$', 'mylessons', name="mylessons"),
    url(r'^profile/(?P<user_id>\d+)/$', 'profile', name="profile"),
    url(r'^profile/$', 'profile', name="self_profile"),
    url(r'^miniprofile/(?P<user_id>\d+)/$', 'miniprofile', name="miniprofile"),
    url(r'^chief-list/$', "cheiflist", name="chieflist"),
    url(r'^add-lesson/$', LessonWizard.as_view(FORMS), name="add-lesson" ),

)
