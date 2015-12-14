from django.shortcuts import render
from django.contrib.auth.models import User, Group
from api.serializers import *
# Create your views here.
from rest_framework import generics
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
        return Response({'token': token.key})


#################  PARENT'S STUDENTS #####################

class MyInfo(generics.ListCreateAPIView):
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
    serializer_class = StudentSerializer

    def get_queryset(self):
        user = self.request.user
        if user.user_type == "parent":
            return Student.objects.filter(parent__id=user.id)



class ParentStudentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        user = self.request.user
        if user.user_type == "parent":
            queryset = Student.objects.filter(parent__id=user.id)
            return queryset

class ParentStudentClassList(generics.ListAPIView):
    serializer_class = ParentSerializer

    def get_queryset(self):
        user = self.request.user
        if user.user_type == "parent":
            cesar = Student.objects.get(first_name="cesar")

            return cesar.school_class.all()


#################  PARENTS #####################
class ParentList(generics.ListAPIView):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class ParentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()


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
    queryset = Parent.objects.all()

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


#################  CLASSES #####################
class ListClasses(generics.ListCreateAPIView):
    serializer_class = SchoolClassSerializer
    queryset = SchoolClass.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class DetailClasses(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SchoolClassSerializer
    queryset = SchoolClass.objects.all()



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




