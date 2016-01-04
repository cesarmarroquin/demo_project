from django.shortcuts import render
from django.contrib.auth.models import User, Group
from api.serializers import *
# Create your views here.
from rest_framework import generics, exceptions
from schools.models import *
from teachers.models import *
from schools.models import *
from parents.models import *
from rest_framework import filters
from rest_framework.authtoken import views
from rest_framework.views import APIView
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
import stripe
stripe.api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2"
from rest_framework.authtoken.views import ObtainAuthToken


############## CUSTOM CODE TO SEND BACK USER ID AND USER TYPE BACK WITH A TOKEN ####################
# class ObtainAuthToken2(APIView):
#     throttle_classes = ()
#     permission_classes = ()
#     parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
#     renderer_classes = (renderers.JSONRenderer,)
#     serializer_class = AuthTokenSerializer
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         user_type = user.user_type
#         user_id = user.id
#         return Response({'token': token.key, 'user_type': user_type, 'id': user_id})


############## CUSTOM CODE TO SEND BACK USER ID AND USER TYPE BACK WITH A TOKEN ####################
class ObtainAuthToken3(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user_type = user.user_type
        user_id = user.id
        return Response({'token': token.key, 'user_type': user_type, 'id': user_id})




#################  PARENTS#####################
class MyInfo(generics.ListCreateAPIView):
    """
    This retrieves basic info for a user such as name and user type.
    """
    serializer_class = ParentSerializer

    def get_queryset(self):
        user = self.request.user
        if user.user_type == "parent":
            self.serializer_class = ParentSerializer
            queryset = Parent.objects.filter(id=user.id)
            return queryset
        elif user.user_type == "teacher":
            self.serializer_class = TeacherSerializer
            queryset = Teacher.objects.filter(id=user.id)
            return queryset



#################  PARENTS #####################
class ParentList(generics.ListCreateAPIView):
    serializer_class = ParentSerializer

    def get_queryset(self):
        user = self.request.user
        return Parent.objects.all()


class ParentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()


class ParentStudentsList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        queryset = Student.objects.filter(parent__id=id)
        return queryset



#################  TEACHERS #####################
class ListTeachers(generics.ListCreateAPIView):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        queryset = Teacher.objects.all()
        return queryset


class DetailTeachers(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class TeacherClassList(generics.ListCreateAPIView):
    serializer_class = SchoolClassSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        queryset = SchoolClass.objects.filter(teacher__id=id)
        return queryset



#################  CLASSES #####################
class ListClasses(generics.ListCreateAPIView):
    serializer_class = SchoolClassSerializer
    queryset = SchoolClass.objects.all()


class DetailClasses(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SchoolClassSerializer
    queryset = SchoolClass.objects.all()


class ClassEventList(generics.ListCreateAPIView):
    serializer_class = ClassEventSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        queryset = ClassEvent.objects.filter(school_class__id = id )
        return queryset


class ClassFeeList(generics.ListCreateAPIView):
    serializer_class = ClassFeeSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        queryset = ClassFee.objects.filter(school_class__id = id )
        return queryset


class ClassStudentList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        queryset = Student.objects.filter(school_class__id = id )
        return queryset



################# STUDENTS #####################
class ListStudents(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class DetailStudents(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentFeeList(generics.ListCreateAPIView):
    serializer_class = ClassFeePaymentSerializer

    def get_queryset(self):
        fee_id = self.kwargs['pk']
        queryset = ClassFeePayment.objects.filter(student__id = fee_id )
        return queryset


class StudentHomeworkList(generics.ListCreateAPIView):
    serializer_class = StudentHomeworkSerializer

    def get_queryset(self):
        homework_id = self.kwargs['pk']
        queryset = StudentHomework.objects.filter(student__id = homework_id )
        return queryset


class StudentFormList(generics.ListCreateAPIView):
    serializer_class = StudentFormSerializer

    def get_queryset(self):
            id = self.kwargs['pk']
            queryset = StudentForm.objects.filter(student__id = id )
            return queryset


class StudentAttendanceList(generics.ListCreateAPIView):
    serializer_class = StudentAttendanceSerializer

    def get_queryset(self):
            id = self.kwargs['pk']
            queryset = StudentAttendance.objects.filter(student__id = id )
            return queryset


class StudentBehaviorList(generics.ListCreateAPIView):
    serializer_class = StudentBehaviorSerializer

    def get_queryset(self):
            id = self.kwargs['pk']
            queryset = StudentBehavior.objects.filter(student__id = id )
            return queryset


#################  SCHOOLS #####################
class ListSchools(generics.ListCreateAPIView):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()


class DetailSchools(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()


class SchoolClassList(generics.ListCreateAPIView):
    serializer_class = SchoolClassSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        queryset = SchoolClass.objects.filter(school__id = id)
        return queryset


class SchoolEventList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SchoolEventSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        queryset = SchoolEvent.objects.filter(school__id = id)
        return queryset



#################  SCHOOL EVENTS #####################
class ListSchoolEvents(generics.ListCreateAPIView):
    serializer_class = SchoolEventSerializer
    queryset = SchoolEvent.objects.all()


class DetailSchoolEvents(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SchoolEventSerializer
    queryset = SchoolEvent.objects.all()



#################  CLASS EVENTS #####################
class ListClassEvents(generics.ListCreateAPIView):
    serializer_class = ClassEventSerializer
    queryset = ClassEvent.objects.all()


class DetailClassEvents(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClassEventSerializer
    queryset = ClassEvent.objects.all()


#################  CLASS FEES #####################
class ListClassFees(generics.ListCreateAPIView):
    serializer_class = ClassFeePaymentSerializer
    queryset = ClassFeePayment.objects.all()


class DetailClassFees(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClassFeePaymentSerializer
    queryset = ClassFeePayment.objects.all()

    def perform_update(self, serializer):
        token = serializer.initial_data['token']
        stripe.api_key = 'sk_test_biD58COvD5uBeTpom2jHDsjT'
        if serializer.initial_data['is_paid'] == True:
            try:
                charge = stripe.Charge.create(
                    amount=serializer.initial_data['amount_needed'],
                    currency="usd",
                    source=token,
                    description="fee payment"
                )
                stripe_charge_id = charge['id']
                serializer.save(charge_id=stripe_charge_id, payment_amount = charge['amount'], is_paid = True)

            except stripe.error.CardError:
                serializer.save(is_paid = False)


class DetailStudentHomework(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentHomeworkSerializer
    queryset = StudentHomework.objects.all()



#################  FORMS #####################
class ListStudentForms(generics.ListCreateAPIView):
    serializer_class = StudentFormSerializer
    queryset = StudentForm.objects.all()


class DetailStudentForms(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentFormSerializer
    queryset = StudentForm.objects.all()



#################  ATTENDANCE #####################
class ListStudentAttendance(generics.ListCreateAPIView):
    serializer_class = StudentAttendanceSerializer
    queryset = StudentAttendance.objects.all()


class DetailStudentAttendance(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentAttendanceSerializer
    queryset = StudentAttendance.objects.all()



#################  BEHAVIOR #####################
class ListStudentBehavior(generics.ListCreateAPIView):
    serializer_class = StudentBehaviorSerializer
    queryset = StudentBehavior.objects.all()


class DetailStudentBehavior(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentBehaviorSerializer
    queryset = StudentBehavior.objects.all()