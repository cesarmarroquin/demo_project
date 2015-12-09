from django.contrib.auth.models import User
from django.db import models
from parents.models import CustomUser
# from users.models import *


class Teacher(CustomUser):
    user_type = "teacher"
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)