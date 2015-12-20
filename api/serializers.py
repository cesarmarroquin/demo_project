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
        fields = ('id','name', 'schoolclass_set', 'schoolevent_set')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','first_name', 'last_name','parent', 'school_class', 'classfeepayment_set', 'studenthomework_set')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id','user_type','first_name', 'last_name', 'picture_url' )


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ('id', 'user_type','first_name', 'last_name', 'student_set', 'picture_url')


class SchoolEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolEvent
        fields = ('id','name','school', 'description', 'date', 'picture_url')


class ClassEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassEvent
        fields = ('id','name','school_class', 'description', 'date', 'picture_url')


class ClassFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassFee
        fields = ('id', 'school_class','name','description','amount','date', 'picture_url')


class ClassFeePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassFeePayment
        fields = ('id', 'student','class_fee','name','description','payment_amount','amount_needed','date', 'picture_url',  'payment_amount','charge_id','refunded','is_paid',)


class ClassHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassHomework
        fields = ('school_class','title','description','picture_url','due_date','points')


class StudentHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentHomework
        fields = ('class_homework','student','title','description','picture_url','due_date','points', )