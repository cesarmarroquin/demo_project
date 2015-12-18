from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# from schools.models import Student
from teachers.models import Teacher
from parents.models import Parent
from schools.models import *
from hellosign_sdk import HSClient
import cloudinary
import cloudinary.uploader
import cloudinary.api

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


@receiver(post_save, sender=ClassForm)
def create_student_form(sender, instance=None, created=False, **kwargs):
    if created:
        for student in Student.objects.filter(school_class__name=instance.school_class.name):
            StudentForm.objects.create(class_form = instance,
                                       student=student,
                                       file = instance.file,
                                       title = instance.title,
                                       subject = instance.subject,
                                       message = instance.message,
                                       signer = Parent.objects.filter(student=student)[0],
                                       due_date = instance.due_date,
                                        )

        # client = HSClient(api_key='7d4094db9ecdb9a58f0edb6a5473755ae8e9968ae354a119f11c4779fd86ae26')
        # client.send_signature_request(
        #         test_mode=True,
        #         title="title=NDA with Acme Co.",
        #         subject="The NDA we talked about",
        #         message="Please sign this NDA and then we can discuss more. Let me know if you have any questions.",
        #         signers=[{ 'email_address': 'cesarm2333@gmail.com', 'name': 'Cesar Marr' }],
        #         files=[instance.file.path]
        #         )



@receiver(post_save, sender=StudentForm)
def check_form_signed(sender, instance=None, created=False, **kwargs):
    client = HSClient(api_key='7d4094db9ecdb9a58f0edb6a5473755ae8e9968ae354a119f11c4779fd86ae26')
    if created:
        # client.get_signature_request('f7e9760622363224832f464267ece894fa39a0fd').json_data.get("is_complete")
        client = HSClient(api_key='7d4094db9ecdb9a58f0edb6a5473755ae8e9968ae354a119f11c4779fd86ae26')
        client.send_signature_request(
                test_mode=True,
                title=instance.title,
                subject=instance.subject,
                message=instance.message,
                signers=[{ 'email_address': instance.signer.email, 'name': instance.signer.first_name }],
                files=[instance.file.path]
                )

@receiver(post_save, sender=Parent)
def upload_picture_cloudinary(sender,instance=None, created=False, **kwargs):
    if created:
        # for parent in Parent.objects.all():
        #     if parent.profile_picture and hasattr(parent.profile_picture, 'path'):
        #         parent.profile_picture.path
        #     else:
        #         print("has no image")

            if instance.profile_picture and hasattr(instance.profile_picture, 'path'):
                print(instance.profile_picture.path)
                # print("it uploaded")
                # print(cloudinary.CloudinaryImage("http://res.cloudinary.com/dpkceqvfi").image(type="fetch"))
                cloudinary.uploader.upload(instance.profile_picture.path)
            else:
                print("has no image")

