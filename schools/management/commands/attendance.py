from django.core.management.base import BaseCommand
from schools.models import *
from django.utils import timezone
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


class Command(BaseCommand):
    args = 'Arguments is not needed'
    help = 'Django admin custom command poc.'

    def handle(self, *args, **options):
        for school_class in SchoolClass.objects.all():
            for student in Student.objects.filter(school_class=school_class):
                StudentAttendance.objects.create(student=student,
                                                 school_class=school_class,
                                                 )