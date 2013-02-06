from django.contrib import admin

from django.contrib.auth. admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import User

from forms import RegistrationForm

from app.models import Profile, Customer



class UserProfileInline(admin.StackedInline):
    model = Profile
    max_num = 1
    can_delete = False

class CustomerInline(admin.StackedInline):
    model = Customer
    max_num = 1
    can_delete = False


class UserAdmin(AuthUserAdmin):

    inlines = [UserProfileInline, CustomerInline]

    def response_add(self, request, obj, **kwargs):
        Profile.objects.create(user=obj)
        return super(AuthUserAdmin, self).response_add(request, obj, **kwargs)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
