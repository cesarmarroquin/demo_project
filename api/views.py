from django.shortcuts import render
from django.contrib.auth.models import User, Group
from api.serializers import *
# Create your views here.
from rest_framework import generics
from schools.models import *
from teachers.models import *
from schools.models import *

#################  PARENT #####################
class ListParents(generics.ListCreateAPIView):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class DetailParents(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()

#################  TEACHERS #####################
class ListTeachers(generics.ListCreateAPIView):
    serializer_class = TeacherSerializer
    queryset = Parent.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class DetailTeachers(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializer
    queryset = Parent.objects.all()

################# STUDENTS #####################
class ListStudents(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Parent.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class DetailStudents(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Parent.objects.all()

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
    queryset = Parent.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class DetailClasses(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SchoolClassSerializer
    queryset = Parent.objects.all()