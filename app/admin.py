from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Home, HomeBlock


admin.site.register(Author, PageAdmin)
