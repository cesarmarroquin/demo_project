from django.contrib.auth.models import User
from django.db import models
from parents.models import CustomUser
# from users.models import *


class Teacher(CustomUser):
    user_type = "teacher"
    profile_picture = models.ImageField(upload_to='parent_profile_pictures', blank=True, null=True)
    picture_url = models.URLField(default="http://res.cloudinary.com/dpkceqvfi/image/upload/v1450429700/default_profile_ru96fo.png")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)

