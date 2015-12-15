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


class ObtainAuthToken2(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user_type = user.user_type
        return Response({'token': token.key, 'user_type': user_type})



#################  PARENTS#####################

class MyInfo(generics.ListCreateAPIView):
    """
    This retrieves basic info for a user such as name and user type.
    """
    serializer_class = ParentSerializer

    def get_queryset(self):
        user = self.request.user
        print(user.user_type)

        if user.user_type == "parent":
            self.serializer_class = ParentSerializer
            queryset = Parent.objects.filter(id=user.id)
            return queryset
        elif user.user_type == "teacher":
            self.serializer_class = TeacherSerializer
            queryset = Teacher.objects.filter(id=user.id)
            return queryset


class ParentStudentList(generics.ListCreateAPIView):
    """
    This retrieves a list of all children for a parent
    """
    serializer_class = StudentSerializer

    def get_queryset(self):
        user = self.request.user
        if user.user_type == "parent":
            return Student.objects.filter(parent__id=user.id)
        else:
            raise exceptions.AuthenticationFailed('You must be signed in')



class ParentStudentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This retrieves a detail of a child for a parent
    """
    serializer_class = StudentSerializer

    def get_queryset(self):
        user = self.request.user
        if user.user_type == "parent":
            queryset = Student.objects.filter(parent__id=user.id)
            return queryset
        else:
            raise exceptions.AuthenticationFailed('You must be signed in')

class ParentStudentClassList(generics.ListAPIView):
    """
    This retrieves a list of all classes for a child if user is parent
    """
    serializer_class = SchoolClassSerializer

    def get_queryset(self):
        user = self.request.user
        if user.user_type == "parent":
            queryset = SchoolClass.objects.filter(student__parent__id=user.id)
        else:
            raise exceptions.AuthenticationFailed('You must be signed in')
        return queryset


class ParentStudentClassDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This retrieves a list of all classes for a child if user is parent
    Retrives a list of all classes for a teacher if the user is a teacher
    """
    serializer_class = SchoolClassSerializer

    def get_queryset(self):
        user = self.request.user
        if user.user_type == "parent":
            queryset = SchoolClass.objects.filter(student__parent__id=user.id)
        elif user.user_type == "teacher":
            queryset = SchoolClass.objects.filter(teacher__id=user.id)
        else:
            queryset = None
        return queryset




























#################  PARENTS #####################
class ParentList(generics.ListCreateAPIView):
    serializer_class = ParentSerializer
    # queryset = Parent.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Parent.objects.all()



class ParentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()

class ParentStudentsList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Student.objects.filter(parent__id=user.id)
        return queryset




#################  TEACHERS #####################
class ListTeachers(generics.ListCreateAPIView):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        queryset = Teacher.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset


class DetailTeachers(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class TeacherClassList(generics.ListCreateAPIView):
    serializer_class = SchoolClassSerializer

    def get_queryset(self):
        user = self.request.user
        if user.user_type == "teacher":
            queryset = SchoolClass.objects.filter(teacher__id=user.id)
            return queryset
        else:
            raise exceptions.AuthenticationFailed('You must be signed in')



#################  CLASSES #####################
class ListClasses(generics.ListCreateAPIView):
    serializer_class = SchoolClassSerializer
    queryset = SchoolClass.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class DetailClasses(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SchoolClassSerializer
    def get_queryset(self):
        id = self.kwargs['pk']
        print(id)
        queryset = SchoolClass.objects.all()
        return queryset


class ClassEventList(generics.ListCreateAPIView):
    serializer_class = ClassEventSerializer

    def get_queryset(self):
        class_id = self.kwargs['pk']
        print(id)
        queryset = ClassEvent.objects.filter(school_class__id = class_id )
        return queryset


class ClassFeeList(generics.ListCreateAPIView):
    serializer_class = ClassFeeSerializer

    def get_queryset(self):
        class_id = self.kwargs['pk']
        print(id)
        queryset = ClassFee.objects.filter(school_class__id = class_id )
        return queryset


class ClassStudentList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        class_id = self.kwargs['pk']
        print(id)
        queryset = Student.objects.filter(school_class__id = class_id )
        return queryset



################# STUDENTS #####################
class ListStudents(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class DetailStudents(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

#################  SCHOOLS #####################
class ListSchools(generics.ListCreateAPIView):
    serializer_class = SchoolSerializer
    queryset = Parent.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class DetailSchools(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SchoolSerializer
    queryset = Parent.objects.all()





#################  SCHOOL EVENTS #####################
class ListSchoolEvents(generics.ListCreateAPIView):
    serializer_class = SchoolEventSerializer
    queryset = SchoolEvent.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class DetailSchoolEvents(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SchoolEventSerializer
    queryset = SchoolEvent.objects.all()



#################  CLASS EVENTS #####################
class ListClassEvents(generics.ListCreateAPIView):
    serializer_class = ClassEventSerializer
    queryset = ClassEvent.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class DetailClassEvents(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClassEventSerializer
    queryset = ClassEvent.objects.all()




