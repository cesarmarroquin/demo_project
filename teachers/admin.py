from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from teachers.models import *

# @admin.register(Teacher)
# class TeacherAdmin(admin.ModelAdmin):
#     fields = ('first_name', 'last_name', 'username', 'password' ,'user_type')

class TeacherAdmin(UserAdmin):
    pass
admin.site.register(Teacher, TeacherAdmin)
