from django.conf.urls.defaults import *

urlpatterns = patterns('app.views',
    url(r'^lessons/$', 'lessons', name="lessons"),
)
