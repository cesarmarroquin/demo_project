from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from parents.models import *
from django import forms

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'username', 'password', 'user_type')


