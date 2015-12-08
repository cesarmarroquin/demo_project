from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)