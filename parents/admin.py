from django.contrib import admin
from parents.models import *

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name')
