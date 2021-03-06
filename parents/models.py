from django.contrib.auth.models import AbstractUser
from django.db import models
# from users.models import CustomUser
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    type_choices = (
        ('parent', 'parent user'),
        ('teacher', 'teacher user'),
        ('admin', 'admin user'),
    )

    user_type = models.CharField(max_length=7,
                                 choices=
                                 type_choices,
                                 default='parent')


class Parent(CustomUser):
    user_type = "parent"
    profile_picture = models.ImageField(upload_to='parent_profile_pictures', blank=True, null=True)
    picture_url = models.URLField(default="http://res.cloudinary.com/dpkceqvfi/image/upload/v1450429700/default_profile_ru96fo.png")
    phone_number = PhoneNumberField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)