from django.contrib.auth.models import User
from rest_framework import serializers
from schools.models import *
from parents.models import *
from teachers.models import *

############## SCHOOL  #####################
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id','name', 'schoolclass_set', 'schoolevent_set')


class SchoolEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolEvent
        fields = ('id','name','school', 'description', 'date', 'picture_url')



############## PARENT  #####################
class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ('id', 'user_type','first_name', 'last_name', 'student_set', 'picture_url', 'phone_number', 'email')



############## TEACHER  #####################
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id','user_type','first_name', 'last_name', 'picture_url', 'phone_number','email')



##############  CLASS  #####################
class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = ('id','name', 'teacher', 'school', 'classevent_set', 'classfee_set', 'student_set')


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
        fields = ('id', 'student','class_fee','name','description','payment_amount','amount_needed','date',
                  'picture_url',  'payment_amount','charge_id','refunded','is_paid',)


class ClassHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassHomework
        fields = ('id','school_class','title','description','picture_url','due_date','points', )


class ClassFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassForm
        fields =('id','school_class','file','title','subject' ,'message','due_date')



############## STUDENT  #####################
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','first_name', 'last_name','parent','picture_url', 'school_class', 'classfeepayment_set', 'studenthomework_set',
                  'studentform_set', 'studentattendance_set', 'studentbehavior_set')


class StudentHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentHomework
        fields = ('id','class_homework','student','title','description','picture_url','due_date','points',
                  'total_points','grade', )


class StudentFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentForm
        fields = ('id','class_form', 'student','sign_url','file','title','subject' ,'message','signer', 'viewed', 'view_count',
                  'signed')


class StudentAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendance
        fields = ('id','student', 'school_class', 'date', 'absent', 'tardy')


class StudentBehaviorSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentBehavior
        fields = ('id','student','school_class', 'date', 'good_behavior', 'description')