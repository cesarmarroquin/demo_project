from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# from schools.models import Student
from teachers.models import Teacher
from parents.models import Parent
from schools.models import *

@receiver(post_save)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    list_of_models = ('Teacher', 'Parent',)
    if sender.__name__ in list_of_models:
        if created:
            Token.objects.create(user=instance)

@receiver(post_save, sender=ClassFee)
def create_student_fees(sender,instance=None, created=False, **kwargs):
    if created:
        for student in Student.objects.filter(school_class__name=instance.school_class.name):
            ClassFeePayment.objects.create(student=student,
                                           class_fee =instance,
                                           name = instance.name,
                                           description = instance.description,
                                           image = instance.image,
                                           date = instance.date,
                                           amount_needed = instance.amount,
                                          )

@receiver(post_save, sender=ClassHomework)
def create_student_homework(sender, instance=None, created=False, **kwargs):
    if created:
        for student in Student.objects.filter(school_class__name=instance.school_class.name):
            StudentHomework.objects.create(student=student,
                                           class_homework = instance,
                                           title = instance.title,
                                           description = instance.description,
                                           image = instance.image,
                                           due_date = instance.due_date,
                                           )

