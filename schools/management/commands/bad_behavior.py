from django.core.management.base import BaseCommand
from schools.models import *
from django.utils import timezone


class Command(BaseCommand):
    args = 'Arguments is not needed'
    help = 'Django admin custom command poc.'

    def handle(self, *args, **options):
        for behavior in StudentBehavior.objects.all():
            if behavior.good_behavior == False:
                print("{}, was bad today".format(behavior.student))
                #### send twilio message
                ### send sendgrid message
            else:
                 print("{}, was good today".format(behavior.student))