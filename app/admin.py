from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Home, HomeBlock, Lesson, Step, About, FeaturedChef, LessonIngredient
from .models import Ingredient, Tool, DietaryRestrictions, Cuisine, Course, Video



class HomeBlockAdmin(admin.TabularInline):
    model = HomeBlock

class HomeAdmin(PageAdmin):
    inlines = (HomeBlockAdmin,)

class StepAdmin(admin.TabularInline):
    model = Step

class LessonIngredientAdmin(admin.TabularInline):
    model = LessonIngredient


class LessonAdmin(admin.ModelAdmin):
    inlines = (StepAdmin,LessonIngredientAdmin)

class FeaturedChefAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):

        field = super(FeaturedChefAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == 'chef':
            field.queryset = field.queryset.filter(profile__professional_chef = True)

        return field



admin.site.register(Home, HomeAdmin)
admin.site.register(About, PageAdmin)
admin.site.register(FeaturedChef, FeaturedChefAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(DietaryRestrictions, admin.ModelAdmin)
admin.site.register(Ingredient, admin.ModelAdmin)
admin.site.register(Tool, admin.ModelAdmin)
admin.site.register(Course, admin.ModelAdmin)
admin.site.register(Cuisine, admin.ModelAdmin)
admin.site.register(Video, admin.ModelAdmin)
