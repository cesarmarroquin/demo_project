from django.contrib.auth.models import AbstractUser
from django.db import models
# from users.models import CustomUser

class CustomUser(AbstractUser):
    type_choices = (
        ('parent', 'parent user'),
        ('teacher', 'teacher user'),
        ('admin', 'admin user'),
    )
    user_type = models.CharField(max_length=7,
                                 choices=type_choices,
                                 default='parent')


class Parent(CustomUser):
    user_type = "parent"
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)