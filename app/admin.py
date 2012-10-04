from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Home, HomeBlock


class HomeBlockAdmin(admin.TabularInline):
    model = HomeBlock

class HomeAdmin(PageAdmin):
    inlines = (HomeBlockAdmin,)

admin.site.register(Home, HomeAdmin)
