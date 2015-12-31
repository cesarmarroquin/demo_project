from django.core.management.base import BaseCommand
from schools.models import *
from django.utils import timezone


class Command(BaseCommand):
    args = 'Arguments is not needed'
    help = 'Django admin custom command poc.'

    def handle(self, *args, **options):
        for attendance in StudentAttendance.objects.all():
            if attendance.absent == True:
                print("{}, was absent".format(attendance.student))
                #### send twilio message
                ### send sendgrid message
            else:
                 print("{}, was not absent".format(attendance.student))