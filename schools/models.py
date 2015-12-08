from django.contrib.auth.models import User
from django.db import models
from parents.models import *
from teachers.models import *


class SchoolClass(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

    @property
    def all_teachers(self):
        return self.teacher


class School(models.Model):
    name = models.CharField(max_length=255)
    school_class = models.ForeignKey(SchoolClass)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    parent = models.ManyToManyField(Parent)
    school_class = models.ManyToManyField(SchoolClass)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)


