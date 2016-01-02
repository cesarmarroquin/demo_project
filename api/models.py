from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from teachers.models import Teacher
from parents.models import Parent
from schools.models import *
from hellosign_sdk import HSClient
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.core.mail import send_mail
from twilio.rest import TwilioRestClient

account = "ACcc7711574bd107f0b0dca098020b4b67"
token = "709fd183d70712788b8fc6c1ac045625"
client = TwilioRestClient(account, token)


@receiver(post_save)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    list_of_models = ('Teacher', 'Parent',)
    if sender.__name__ in list_of_models:
        if created:
            Token.objects.create(user=instance)


@receiver(post_save, sender=ClassFee)
def create_student_fees(sender, instance=None, created=False, **kwargs):
    if created:
        for student in Student.objects.filter(school_class__name=instance.school_class.name):
            ClassFeePayment.objects.create(student=student,
                                           class_fee=instance,
                                           name=instance.name,
                                           description=instance.description,
                                           image=instance.image,
                                           date=instance.date,
                                           amount_needed=instance.amount,
                                           )
            for parent in student.parent.filter(student=student):
                send_mail("new fee",
                          "{}, has a new {}. \n{}. It will be {}, and it is due on {},  ".format(student.first_name,
                                                                                                 instance.name,
                                                                                                 instance.description,
                                                                                                 instance.amount,
                                                                                                 instance.date),
                          "Cesar Marroquin <cesarm2333@gmail.com>",
                          ["{}".format(parent.email)])



                message = client.messages.create(to="+1{}".format(parent.phone_number.national_number),
                                                 from_="+17023235267",
                                                 body="{}, has a new {}. \n{}. It will be {}, and it is due on {},  ".format(
                                                         student.first_name, instance.name, instance.description,
                                                         instance.amount, instance.date))


@receiver(post_save, sender=ClassHomework)
def create_student_homework(sender, instance=None, created=False, **kwargs):
    if created:
        for student in Student.objects.filter(school_class__name=instance.school_class.name):
            StudentHomework.objects.create(student=student,
                                           class_homework=instance,
                                           title=instance.title,
                                           description=instance.description,
                                           image=instance.image,
                                           file=instance.file,
                                           due_date=instance.due_date,
                                           total_points=instance.points,
                                           )


@receiver(post_save, sender=StudentHomework)
def update_grades(sender, instance=None, created=False, **kwargs):
    tenth = instance.total_points * 0.1
    print(tenth)
    if instance.points >= instance.total_points - tenth:
        instance.grade = 'A'
    elif instance.points >= (instance.total_points - (tenth * 2)):
        instance.grade = 'B'
    elif instance.points >= (instance.total_points - (tenth * 3)):
        instance.grade = 'C'
    elif instance.points >= (instance.total_points - (tenth * 4)):
        instance.grade = 'D'
    else:
        instance.grade = 'F'


@receiver(post_save, sender=ClassForm)
def create_student_form(sender, instance=None, created=False, **kwargs):
    if created:
        for student in Student.objects.filter(school_class__name=instance.school_class.name):
            StudentForm.objects.create(class_form=instance,
                                       student=student,
                                       file=instance.file,
                                       title=instance.title,
                                       subject=instance.subject,
                                       message=instance.message,
                                       signer=Parent.objects.filter(student=student)[0],
                                       due_date=instance.due_date,
                                       )
            


@receiver(post_save, sender=StudentForm)
def check_form_signed(sender, instance=None, created=False, **kwargs):
    client = HSClient(api_key='7d4094db9ecdb9a58f0edb6a5473755ae8e9968ae354a119f11c4779fd86ae26')
    if created:
        client.send_signature_request(
                test_mode=True,
                title=instance.title,
                subject=instance.subject,
                message=instance.message,
                signers=[{'email_address': instance.signer.email, 'name': instance.signer.first_name}],
                files=[instance.file.path]
        )


@receiver(post_save, sender=Parent)
def upload_picture_cloudinary(sender, instance=None, created=False, **kwargs):
    if created:
        if instance.profile_picture and (hasattr(instance.profile_picture, 'path')):
            image = cloudinary.uploader.upload(instance.profile_picture.path)
            if instance.profile_picture != "http://res.cloudinary.com/dpkceqvfi/image/upload/v1450429700/default_profile_ru96fo.png":
                print("original url" + instance.picture_url)
                instance.picture_url = image.get('url')
                print("this is the new url" + instance.picture_url)
                instance.save()
        else:
            print("has no image")
