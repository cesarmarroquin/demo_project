from django.contrib.auth.models import User
from rest_framework import serializers
from schools.models import *
from parents.models import *
from teachers.models import *

class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = ('id','name', 'teacher', 'school', 'classevent_set', 'classfee_set', 'student_set')

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id','name', 'schoolclass_set')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','first_name', 'last_name','parent', 'school_class', 'classfeepayment_set')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id','user_type','first_name', 'last_name', )

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ('id', 'user_type','first_name', 'last_name', 'student_set')


class SchoolEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolEvent
        fields = ('id','name','school', 'description', 'date', 'image')

class ClassEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassEvent
        fields = ('id','name','school_class', 'description', 'date', 'image')

class ClassFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassFee
        fields = ('id', 'school_class','name','description','amount','date', 'image')
