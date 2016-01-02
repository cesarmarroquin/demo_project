from django.core.management.base import BaseCommand
from schools.models import *
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
from twilio.rest import TwilioRestClient
account = "ACcc7711574bd107f0b0dca098020b4b67"
token = "709fd183d70712788b8fc6c1ac045625"
client = TwilioRestClient(account, token)
class Command(BaseCommand):
    args = 'Arguments is not needed'
    help = 'Django admin custom command poc.'

    def handle(self, *args, **options):
        for attendance in StudentAttendance.objects.all():
            if attendance.absent == True:
                for parent in attendance.student.parent.filter(student=attendance.student):
                    print("{}, was absent".format(attendance.student))
                    ### send email to parent when child is absent
                    send_mail("Your Student was Absent",
                              "{}, was absent today from {}".format(attendance.student, attendance.school_class),
                              "Cesar Marroquin <cesarm2333@gmail.com>",
                              ["{}".format(parent.email)])

                    #### send text to parent when child is absent
                    message = client.messages.create(to="+1{}".format(parent.phone_number.national_number), from_="+17023235267",
                                                     body="{}, your child {}, was absent today from {}".format(parent.first_name, attendance.student, attendance.school_class))


            elif attendance.tardy == True:
                for parent in attendance.student.parent.filter(student=attendance.student):
                    print("{}, was tardy".format(attendance.student))
                    ### send email to parent when child is absent
                    send_mail("Your Student was Tardy",
                              "{}, was tardy today in {}".format(attendance.student, attendance.school_class),
                              "Cesar Marroquin <cesarm2333@gmail.com>",
                              ["{}".format(parent.email)])

                    #### send text to parent when child is absent
                    message = client.messages.create(to="+1{}".format(parent.phone_number.national_number), from_="+17023235267",
                                                     body="{}, was tardy today in {}".format(attendance.student, attendance.school_class))