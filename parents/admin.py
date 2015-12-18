from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from parents.models import *
from django import forms
from schools.models import *

# @admin.register(Parent)
# class ParentAdmin(UserAdmin):
#     fields = ('first_name', 'last_name', 'username', 'password', 'user_type')


class ParentAdmin(UserAdmin):
    UserAdmin.list_display += ('profile_picture',)
    UserAdmin.add_fieldsets += (
            (None, {'fields': ('profile_picture',)}),
    )

    # fields = ('user_type','first_name', 'last_name', 'student_set', 'profile_picture')
    pass
admin.site.register(Parent, ParentAdmin)



