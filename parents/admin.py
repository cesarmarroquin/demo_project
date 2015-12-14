from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from parents.models import *
from django import forms
from schools.models import *

# @admin.register(Parent)
# class ParentAdmin(UserAdmin):
#     fields = ('first_name', 'last_name', 'username', 'password', 'user_type')


class ParentAdmin(UserAdmin):
    pass
admin.site.register(Parent, ParentAdmin)



