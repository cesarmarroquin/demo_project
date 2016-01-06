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



###################  Text/Email Notification Function #################################
def send_text_email(subject,message,stu_parent):
    """
    This function sends out texts and emails to a parent

    :param subject: this will be the subject of the email
    :param message: this will be the main body of both the email and text message
    :param stu_parent: this should be the parent it will be sent to
    :return:
    """
    ### send email to parent when child is absent
    send_mail(subject, message, "Cesar Marroquin <cesarm2333@gmail.com>",["{}".format(stu_parent.email)])
    #### send text to parent when child is absent
    client = TwilioRestClient(os.environ['TWILIO_ACCOUNT_ID'], os.environ['TWILIO_TOKEN'])
    text = client.messages.create(to="+1{}".format(stu_parent.phone_number.national_number),from_="+17023235267",body=message)



###################   Token Creation #################################
@receiver(post_save)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    list_of_models = ('Teacher', 'Parent',)
    if sender.__name__ in list_of_models:
        if created:
            Token.objects.create(user=instance)



####################  Users ##########################################
@receiver(post_save, sender=Parent)
def upload_picture_cloudinary(sender, instance=None, created=False, **kwargs):
    if created:
        if instance.profile_picture and (hasattr(instance.profile_picture, 'path')):
            image = cloudinary.uploader.upload(instance.profile_picture.path)
            if instance.profile_picture != "http://res.cloudinary.com/dpkceqvfi/image/upload/v1450429700/default_profile_ru96fo.png":
                instance.picture_url = image.get('url')
                instance.save()



####################  Attendance ##########################################
@receiver(post_save, sender=StudentAttendance)
def notify_absent_tardy(sender, instance=None, created=False, **kwargs):
        if instance.absent == True:
            for parent in instance.student.parent.filter(student=instance.student):
                subject = "Your Student was Absent"
                message = "{}, was absent today from {}".format(instance.student, instance.school_class)
                send_text_email(subject,message,parent)

        elif instance.tardy == True:
            for parent in instance.student.parent.filter(student=instance.student):
                subject = "Your Student was Tardy"
                message = "{}, was tardy today in {}".format(instance.student, instance.school_class)
                send_text_email(subject,message,parent)



####################  Behavior ##########################################
@receiver(post_save, sender=StudentBehavior)
def notify_bad_behavior(sender, instance=None, created=False, **kwargs):
    if instance.good_behavior == False:
        for parent in instance.student.parent.filter(student=instance.student):
            subject = "Your Student was behaving badly today"
            message = "{}, was behaving badly today in {}".format(instance.student, instance.school_class)
            send_text_email(subject,message,parent)



####################  Grades ##########################################
@receiver(post_save, sender=StudentHomework)
def update_grades(sender, instance=None, created=False, **kwargs):
    tenth = instance.total_points * 0.1
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


@receiver(post_save, sender=StudentHomework)
def notify_bad_grade(sender, instance=None, created=False, **kwargs):
    if not created:
        if instance.grade == 'F':
            for parent in instance.student.parent.filter(student=instance.student):
                subject = "Your Child failed an assignment today"
                message = '{}, your child {}, recieved an F on an assignment. The assignment is titled: "{}", and is ' \
                          'from his {} class'.format(parent.first_name, instance.student,
                                                     instance.title,instance.class_homework.school_class)
                send_text_email(subject,message,parent)



####################  Homework ##########################################
@receiver(post_save, sender=ClassHomework)
def create_student_homework(sender, instance=None, created=False, **kwargs):
    if created:
        for student in Student.objects.filter(school_class__name=instance.school_class.name):
            StudentHomework.objects.create(student=student,class_homework=instance,
                                           title=instance.title,description=instance.description,
                                           image=instance.image,file=instance.file,
                                           due_date=instance.due_date,total_points=instance.points,
                                           )

            for parent in student.parent.filter(student=student):
                subject = "new homework"
                message =  '{}, has a new a homework assignment in {}. It is titled "{}".'.format(student.first_name,
                                                                                                instance.school_class,
                                                                                                instance.title)
                send_text_email(subject,message,parent)



####################  Fees ##########################################
@receiver(post_save, sender=ClassFee)
def create_student_fees(sender, instance=None, created=False, **kwargs):
    if created:
        for student in Student.objects.filter(school_class__name=instance.school_class.name):
            ClassFeePayment.objects.create(student=student,class_fee=instance,
                                           name=instance.name,description=instance.description,
                                           image=instance.image,date=instance.date,
                                           amount_needed=instance.amount,
                                           )
            for parent in student.parent.filter(student=student):
                subject = "new fee"
                message = "{}, has a new {}. \n{}. It will be {}, and it is due on {},  ".format(student.first_name,
                                                                                                 instance.name,
                                                                                                 instance.description,
                                                                                                 instance.amount,
                                                                                                 instance.date),
                send_text_email(subject,message,parent)
    else:
        for student_fee in ClassFeePayment.objects.filter(class_fee=instance):
            student_fee.name=instance.name
            student_fee.description = instance.description
            student_fee.image = instance.description
            student_fee.date = instance.date
            student_fee.amount_needed = instance.amount



####################  Forms ##########################################
@receiver(post_save, sender=ClassForm)
def create_student_form(sender, instance=None, created=False, **kwargs):
    if created:
        for student in Student.objects.filter(school_class__name=instance.school_class.name):
            StudentForm.objects.create(class_form=instance,student=student,file=instance.file,title=instance.title,
                                       subject=instance.subject,message=instance.message,
                                       signer=Parent.objects.filter(student=student)[0],due_date=instance.due_date,
                                       )

            for parent in student.parent.filter(student=student):
                subject = "new form"
                message = "{}, has a new form that requires a signature. \n{}. Please check your email for a hello sign " \
                          "email and sign the form online".format(student.first_name,instance.message,),
                send_text_email(subject,message,parent)


@receiver(post_save, sender=StudentForm)
def check_form_signed(sender, instance=None, created=False, **kwargs):
    client = HSClient(api_key=os.environ['HELLO_SIGN_API_KEY'])
    if created:
        client.send_signature_request(
                test_mode=True,title=instance.title,
                subject=instance.subject,message=instance.message,
                signers=[{'email_address': instance.signer.email, 'name': instance.signer.first_name}],files=[instance.file.path]
        )



####################  Events ##########################################
@receiver(post_save, sender=ClassEvent)
def notify_new_event(sender, instance=None, created=False, **kwargs):
        for student in Student.objects.filter(school_class=instance.school_class):
            for parent in student.parent.filter(student=student):
                subject = "There is a new event"
                message = "{}, has a new event in {} class".format(student, instance.school_class)
                send_text_email(subject,message,parent)