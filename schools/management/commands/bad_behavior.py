from django.core.management.base import BaseCommand
from schools.models import *
from django.utils import timezone
from django.core.mail import send_mail
from twilio.rest import TwilioRestClient
account = "ACcc7711574bd107f0b0dca098020b4b67"
token = "709fd183d70712788b8fc6c1ac045625"
client = TwilioRestClient(account, token)


class Command(BaseCommand):
    args = 'Arguments is not needed'
    help = 'Django admin custom command poc.'

    def handle(self, *args, **options):
        for behavior in StudentBehavior.objects.all():
            if behavior.good_behavior == False:
                print("{}, was bad today".format(behavior.student))
                for parent in behavior.student.parent.filter(student=behavior.student):
                    print("{}, was behaving badly today".format(behavior.student))
                    ### send email to parent when child is absent
                    send_mail("Your Student was behaving badly today",
                              "{}, was behaving badly today in {}".format(behavior.student, behavior.school_class),
                              "Cesar Marroquin <cesarm2333@gmail.com>",
                              ["{}".format(parent.email)])

                    #### send text to parent when child is absent
                    message = client.messages.create(to="+1{}".format(parent.phone_number.national_number), from_="+17023235267",
                                                     body="{}, your child {}, was behaving badly today in {}".format(parent.first_name, behavior.student, behavior.school_class))
            else:
                 print("{}, was good today".format(behavior.student))