from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Home, HomeBlock, Lesson, Recipie


class HomeBlockAdmin(admin.TabularInline):
    model = HomeBlock

class HomeAdmin(PageAdmin):
    inlines = (HomeBlockAdmin,)


admin.site.register(Home, HomeAdmin)
admin.site.register(Lesson, admin.ModelAdmin)
admin.site.register(Recipie, admin.ModelAdmin)
