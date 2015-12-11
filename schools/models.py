from django.contrib.auth.models import User
from django.db import models
from parents.models import *
from teachers.models import *


class School(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)


class SchoolClass(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher)
    school = models.ForeignKey(School, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{}".format(self.name)


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    parent = models.ManyToManyField(Parent)
    school_class = models.ManyToManyField(SchoolClass)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)


# class Homework(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()

#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return "{}".format(self.name)

class SchoolEvent(models.Model):
    school = models.ForeignKey(School)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='school_event_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)


class ClassEvent(models.Model):
    school_class = models.ForeignKey(SchoolClass)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='class_event_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

# class Form(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return "{}".format(self.name)
#

#
# class SchoolFee(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return "{}".format(self.name)


# class ClassFee(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return "{}".format(self.name)