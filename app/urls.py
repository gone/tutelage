from django.conf.urls.defaults import *

urlpatterns = patterns('app.views',
    url(r'^lessons/$', 'lessons', name="lessons"),
    url(r'^mylessons/$', 'mylessons', name="mylessons"),
    url(r'^profile/(?P<user_id>\d+)/$', 'profile', name="profile"),
    url(r'^profile/$', 'profile', name="self_profile"),

)
