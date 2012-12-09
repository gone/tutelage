from django.contrib import admin

from django.contrib.auth. admin import UserAdmin
from django.contrib.auth.models import User

from forms import RegistrationForm

from app.models import Profile

class MyUserAdmin(UserAdmin):

    def response_add(self, request, obj, **kwargs):
        Profile.objects.create(user=obj)
        return super(UserAdmin, self).response_add(request, obj, **kwargs)

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
