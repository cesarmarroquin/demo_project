from django.contrib.auth.models import User
from rest_framework import serializers
from schools.models import *
from parents.models import *
from teachers.models import *

class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = ('name',)

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('name',)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name',)


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name')

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ('first_name', 'last_name')