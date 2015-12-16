from django.contrib.auth.models import User
from django.db import models
from parents.models import *
from teachers.models import *
import stripe

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
    # school_fee = models.ForeignKey(SchoolFee)
    # class_fee = models.ForeignKey(ClassFee)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)


class ClassHomework(models.Model):
    school_class = models.ForeignKey(SchoolClass)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='class_homework_images', blank=True, null=True)
    due_date = models.DateField()
    points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)

class StudentHomework(models.Model):
    class_homework = models.ForeignKey(ClassHomework)
    student = models.ForeignKey(Student)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='class_homework_images', blank=True, null=True)
    due_date = models.DateField()
    points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)

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


# class SchoolFee(models.Model):
#     school = models.ForeignKey(School)
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     amount = models.DecimalField(max_digits=9, decimal_places=2)
#     charge_id = models.CharField(max_length=255, null=True)
#     refunded = models.BooleanField(default=False)
#     image = models.ImageField(upload_to='school_fee_images', blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return "{}".format(self.name)

#
class ClassFee(models.Model):
    school_class = models.ForeignKey(SchoolClass)
    name = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to='class_fee_images', blank=True, null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

class ClassFeePayment(models.Model):
    student = models.ForeignKey(Student)
    class_fee = models.ForeignKey(ClassFee)
    payment_amount = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    charge_id = models.CharField(max_length=255, null=True)
    refunded = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def refund(self):
        re = stripe.Refund.create(charge= self.charge.id)
        self.refunded = True

    def __str__(self):
        return "{}, {}, paid = {}".format(self.class_fee, self.payment_amount, self.is_paid)