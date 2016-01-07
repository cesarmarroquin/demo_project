from django.shortcuts import render
from django.contrib.auth.models import User, Group
from schools.serializers import *
# Create your views here.
from rest_framework import generics, exceptions
from schools.models import *
from teachers.models import *
from schools.models import *
from parents.models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
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
class ObtainAuthToken3(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user_type = user.user_type
        user_id = user.id
        return Response({'token': token.key, 'user_type': user_type, 'id': user_id})



#################  USER INFO  #####################
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

    """
    endpoint that lists all parents
    """
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ParentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This view retrieves one specific parent
    """
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ParentStudentsList(generics.ListCreateAPIView):
    """
    This view retrieves all the students for a parent
    """
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        id = self.kwargs['pk']
        queryset = Student.objects.filter(parent__id=id)
        return queryset



#################  TEACHERS #####################
class ListTeachers(generics.ListCreateAPIView):
    """
    This view retrieves all Teachers
    """
    serializer_class = TeacherSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = Teacher.objects.all()
        return queryset


class DetailTeachers(generics.RetrieveUpdateDestroyAPIView):
    """
     This view retrieves one specific teacher
    """
    serializer_class = TeacherSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Teacher.objects.all()


class TeacherClassList(generics.ListCreateAPIView):
    """
    This view retrieves all the classes for a teacher
    """
    serializer_class = SchoolClassSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        id = self.kwargs['pk']
        queryset = SchoolClass.objects.filter(teacher__id=id)
        return queryset



#################  CLASSES #####################
class ListClasses(generics.ListCreateAPIView):
    """
    This view lists all classes
    """
    serializer_class = SchoolClassSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = SchoolClass.objects.all()


class DetailClasses(generics.RetrieveUpdateDestroyAPIView):
    """
    This view retrieves one specific class
    """
    serializer_class = SchoolClassSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = SchoolClass.objects.all()


class ClassEventList(generics.ListCreateAPIView):
    """
    This view retrieves all the events for a class
    """
    serializer_class = ClassEventSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        id = self.kwargs['pk']
        queryset = ClassEvent.objects.filter(school_class__id = id )
        return queryset


class ClassFeeList(generics.ListCreateAPIView):
    """
    This view retrieves all the fees for a class
    """
    serializer_class = ClassFeeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        id = self.kwargs['pk']
        queryset = ClassFee.objects.filter(school_class__id = id )
        return queryset


class ClassStudentList(generics.ListCreateAPIView):
    """
    This view retrieves all the students for a class
    """
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        id = self.kwargs['pk']
        queryset = Student.objects.filter(school_class__id = id )
        return queryset



################# STUDENTS #####################
class ListStudents(generics.ListCreateAPIView):
    """
    endpoint that lists all students
    """
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class DetailStudents(generics.RetrieveUpdateDestroyAPIView):
    """
    This view retrieves one specific parent
    """
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class StudentFeeList(generics.ListCreateAPIView):
    """
    This view retrieves all the fees for a student
    """
    serializer_class = ClassFeePaymentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        fee_id = self.kwargs['pk']
        queryset = ClassFeePayment.objects.filter(student__id = fee_id )
        return queryset


class StudentHomeworkList(generics.ListCreateAPIView):
    """
    This view retrieves all the homework for a student
    """
    serializer_class = StudentHomeworkSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        homework_id = self.kwargs['pk']
        queryset = StudentHomework.objects.filter(student__id = homework_id )
        return queryset


class StudentFormList(generics.ListCreateAPIView):
    """
    This view retrieves all the forms for a student
    """
    serializer_class = StudentFormSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
            id = self.kwargs['pk']
            queryset = StudentForm.objects.filter(student__id = id )
            return queryset


class StudentAttendanceList(generics.ListCreateAPIView):

    """
    This view retrieves all the attendance objects for a student
    """
    serializer_class = StudentAttendanceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
            id = self.kwargs['pk']
            queryset = StudentAttendance.objects.filter(student__id = id )
            return queryset


class StudentBehaviorList(generics.ListCreateAPIView):
    """
    This view retrieves all the behavior objects for a student
    """
    serializer_class = StudentBehaviorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
            id = self.kwargs['pk']
            queryset = StudentBehavior.objects.filter(student__id = id )
            return queryset


class StudentParentList(generics.ListCreateAPIView):
    """
    This view retrieves all the behavior objects for a student
    """
    serializer_class = ParentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
            id = self.kwargs['pk']
            # queryset = Parent.objects.filter(id_in= id )
            queryset = Parent.objects.filter(id_in=Student.objects.filter(id=id).parent)
            return queryset


#################  SCHOOLS #####################
class ListSchools(generics.ListCreateAPIView):
    """
    endpoint that lists all schools
    """
    serializer_class = SchoolSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = School.objects.all()


class DetailSchools(generics.RetrieveUpdateDestroyAPIView):
    """
    This view retrieves a specific school
    """
    serializer_class = SchoolSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = School.objects.all()


class SchoolClassList(generics.ListCreateAPIView):
    """
    endpoint that lists all classes belonging to a school
    """
    serializer_class = SchoolClassSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        id = self.kwargs['pk']
        queryset = SchoolClass.objects.filter(school__id = id)
        return queryset


class SchoolEventList(generics.ListCreateAPIView):
    """
    endpoint that lists all events for a specific school
    """
    serializer_class = SchoolEventSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        id = self.kwargs['pk']
        queryset = SchoolEvent.objects.filter(school__id = id)
        return queryset



#################  SCHOOL EVENTS #####################
class ListSchoolEvents(generics.ListCreateAPIView):
    """
    endpoint that lists all school events
    """
    serializer_class = SchoolEventSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = SchoolEvent.objects.all()


class DetailSchoolEvents(generics.RetrieveUpdateDestroyAPIView):
    """
    endpoint that retrieves one specific school event
    """
    serializer_class = SchoolEventSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = SchoolEvent.objects.all()



#################  CLASS EVENTS #####################
class ListClassEvents(generics.ListCreateAPIView):
    """
    endpoint that lists all class events
    """
    serializer_class = ClassEventSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ClassEvent.objects.all()


class DetailClassEvents(generics.RetrieveUpdateDestroyAPIView):
    """
    endpoint that retrieves one specific class event
    """
    serializer_class = ClassEventSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ClassEvent.objects.all()


#################  CLASS FEES #####################
class ListClassFees(generics.ListCreateAPIView):
    """
    endpoint that lists all class fees
    """
    serializer_class = ClassFeePaymentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ClassFeePayment.objects.all()


class DetailClassFees(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint that retrieves one specific class fee and also processes a payment transaction for a fee when the is_paid
    attribute is marked to true.  If the card does not work, then the is_paid field is reset to false so that the
    transaction can be attempted again later in the future. It will remain false until the transaction is successfully
    processed.
    """
    serializer_class = ClassFeePaymentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ClassFeePayment.objects.all()

    def perform_update(self, serializer):
        """

        :param serializer:
        :return:
        """
        token = serializer.initial_data['token']
        stripe.api_key = 'sk_test_biD58COvD5uBeTpom2jHDsjT'
        if serializer.initial_data['is_paid']:
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

#################  HOMEWORK #####################
class ListStudentHomework(generics.ListCreateAPIView):
    """
    endpoint that lists all student forms
    """
    serializer_class = StudentHomeworkSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = StudentHomework.objects.all()


class DetailStudentHomework(generics.RetrieveUpdateDestroyAPIView):
    """
    endpoint that retrieves a specific homework object
    """
    serializer_class = StudentHomeworkSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = StudentHomework.objects.all()



#################  FORMS #####################
class ListStudentForms(generics.ListCreateAPIView):
    """
    endpoint that lists all student forms
    """
    serializer_class = StudentFormSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = StudentForm.objects.all()


class DetailStudentForms(generics.RetrieveUpdateDestroyAPIView):
    """
    endpoint that retrieves a specific student form
    """
    serializer_class = StudentFormSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = StudentForm.objects.all()



#################  ATTENDANCE #####################
class ListStudentAttendance(generics.ListCreateAPIView):
    """
    endpoint that lists all attendance objects
    """
    serializer_class = StudentAttendanceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = StudentAttendance.objects.all()


class DetailStudentAttendance(generics.RetrieveUpdateDestroyAPIView):
    """
    endpoint that retrieves a specific attendance object
    """
    serializer_class = StudentAttendanceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = StudentAttendance.objects.all()



#################  BEHAVIOR #####################
class ListStudentBehavior(generics.ListCreateAPIView):
    """
    endpoint that lists all behavior objects
    """
    serializer_class = StudentBehaviorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = StudentBehavior.objects.all()


class DetailStudentBehavior(generics.RetrieveUpdateDestroyAPIView):
    """
    endpoint that retrieces a specific attendance object
    """
    serializer_class = StudentBehaviorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = StudentBehavior.objects.all()