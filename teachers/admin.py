from django.contrib import admin
from teachers.models import *

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'username', 'password')
