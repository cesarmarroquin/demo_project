from django.contrib import admin
from schools.models import *
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('id','first_name', 'last_name', 'parent', 'school_class')


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    fields = ('id','name', 'teacher', 'school',)


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    fields = ('id','name',)
