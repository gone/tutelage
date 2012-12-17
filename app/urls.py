from django.conf.urls.defaults import *


urlpatterns = patterns('app.views',
    url(r'^lessons/$', 'lessons', name="lessons"),
    url(r'^lessons/(?P<lesson_id>\d+)/$', 'lesson_detail', name="lesson_detail"),
    url(r'^mylessons/(?P<user_id>\d+)/$', 'mylessons', name="mylessons"),
    url(r'^profile/(?P<user_id>\d+)/$', 'profile', name="profile"),
    url(r'^profile/$', 'profile', name="self_profile"),
    url(r'^miniprofile/(?P<user_id>\d+)/$', 'miniprofile', name="miniprofile"),
    url(r'^chef-list/$', "cheflist", name="cheflist"),
    url(r'^chefs/$', "featured_chefs", name="featured_chefs"),
    url(r'^ask/submit/$', "ask_form", name="ask_form"),
    url(r'^ask/(?P<slug>[\d\w-]+)?$', "ask", name="ask"),
    url(r'^rate-lesson/(\d+)/([1-5])/$', "rate_lesson", name="rate_lesson"),
    url(r'^add-lesson/(?P<lesson_id>\d+)/ingredients/$', "lesson_ingredients", name="lesson_ingredients"),
    url(r'^add-lesson/(?P<lesson_id>\d+)/steps/$', "lesson_steps", name="lesson_steps"),
    url(r'^add-lesson/(?P<lesson_id>\d+)/video/$', "lesson_video", name="lesson_video"),
    url(r'^add-lesson/(?P<lesson_id>\d+)/$', "add_lesson", name="edit-lesson"),
    url(r'^add-lesson-video/(?P<lesson_id>\d+)/$', "add_lesson_video", name="add-lesson-video"),
    url(r'^add-lesson/$', "add_lesson", name="add-lesson"),
    url(r'^lesson/(?P<lesson_id>\d+)/$', "lesson", name="lesson"),
    url(r'^purchase/(?P<lesson_id>\d+)/$', "purchase", name="purchase"),
)
