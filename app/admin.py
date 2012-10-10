from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Home, HomeBlock, Lesson, Step, About, FeaturedChef


class HomeBlockAdmin(admin.TabularInline):
    model = HomeBlock

class HomeAdmin(PageAdmin):
    inlines = (HomeBlockAdmin,)

class StepAdmin(admin.TabularInline):
    model = Step


class LessonAdmin(admin.ModelAdmin):
    inlines = (StepAdmin,)



admin.site.register(Home, HomeAdmin)
admin.site.register(About, PageAdmin)
admin.site.register(FeaturedChef, PageAdmin)
admin.site.register(Lesson, LessonAdmin)
