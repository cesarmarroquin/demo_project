# from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
#
# class CustomUser(AbstractUser):
#     type_choices = (
#         ('parent', 'parent user'),
#         ('teacher', 'teacher user'),
#         ('admin', 'admin user'),
#     )
#     user_type = models.CharField(max_length=7,
#                                  choices=type_choices,
#                                  default='parent')



# class CustomUserBase(CustomUser):
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return "{}, {}".format(self.last_name, self.first_name)

# class Parent(CustomUserBase):
#     user_type = "parent"
#
# class Teacher(CustomUserBase):
#     user_type = "teacher"
