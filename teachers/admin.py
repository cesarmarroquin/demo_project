from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from teachers.models import *

# @admin.register(Teacher)
# class TeacherAdmin(admin.ModelAdmin):
#     fields = ('first_name', 'last_name', 'username', 'password' ,'user_type')

class TeacherAdmin(UserAdmin):
    # UserAdmin.list_display += ('profile_picture',)
    # UserAdmin.add_fieldsets += (
    #         (None, {'fields': ('profile_picture',)}),
    # )
    pass
admin.site.register(Teacher, TeacherAdmin)
