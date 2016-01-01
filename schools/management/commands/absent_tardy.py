from django.core.management.base import BaseCommand
from schools.models import *
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail


class Command(BaseCommand):
    args = 'Arguments is not needed'
    help = 'Django admin custom command poc.'

    def handle(self, *args, **options):
        for attendance in StudentAttendance.objects.all():
            if attendance.absent == True:
                for parent in attendance.student.parent.filter(student=attendance.student):
                    print("{}, was absent".format(attendance.student))
                    #### send twilio message
                    ### send sendgrid message
                    send_mail("Your Student was Absent",
                              "{}, was absent today from {}".format(attendance.student, attendance.school_class),
                              "Cesar Marroquin <cesarm2333@gmail.com>",
                              ["{}".format(parent.email)])
            elif attendance.tardy == True:
                for parent in attendance.student.parent.filter(student=attendance.student):
                    print("{}, was tardy".format(attendance.student))
                    #### send twilio message
                    ### send sendgrid message
                    send_mail("Your Student was Tardy",
                              "{}, was tardy today from {}".format(attendance.student, attendance.school_class),
                              "Cesar Marroquin <cesarm2333@gmail.com>",
                              ["{}".format(parent.email)])
