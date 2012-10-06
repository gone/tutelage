from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Home, HomeBlock, Lesson, Recipie, About, FeaturedChef


class HomeBlockAdmin(admin.TabularInline):
    model = HomeBlock

class HomeAdmin(PageAdmin):
    inlines = (HomeBlockAdmin,)


admin.site.register(Home, HomeAdmin)
admin.site.register(About, PageAdmin)
admin.site.register(FeaturedChef, PageAdmin)
admin.site.register(Lesson, admin.ModelAdmin)
admin.site.register(Recipie, admin.ModelAdmin)
