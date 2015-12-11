from django.contrib import admin
from schools.models import *
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'parent', 'school_class')


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    fields = ('name', 'teacher', 'school',)


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    fields = ('name',)

@admin.register(SchoolEvent)
class SchoolEventAdmin(admin.ModelAdmin):
    fields = ('name','school', 'description', 'date', 'image')

@admin.register(ClassEvent)
class ClassEventAdmin(admin.ModelAdmin):
    fields = ('name','school_class', 'description', 'date', 'image')
