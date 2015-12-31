from django.core.management.base import BaseCommand
from schools.models import *
from django.utils import timezone


class Command(BaseCommand):
    args = 'Arguments is not needed'
    help = 'Django admin custom command poc.'

    def handle(self, *args, **options):
        for school_class in SchoolClass.objects.all():
            for student in Student.objects.filter(school_class=school_class):
                StudentBehavior.objects.create(student=student,
                                               school_class=school_class,
                                              )