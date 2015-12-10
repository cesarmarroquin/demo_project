from django.shortcuts import render
from django.contrib.auth.models import User, Group
from api.serializers import *
# Create your views here.
from rest_framework import generics
from schools.models import *
from teachers.models import *
from schools.models import *
from rest_framework import filters

#################  PARENT STUDENTS #####################
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


class ParentList(generics.ListAPIView):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()


    def perform_create(self, serializer):
        serializer.save()

class ParentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()
























        # elif username is not None and user_type == "teacher":
        #     queryset = queryset.filter(school_class__teacher__username=username)
        #     print(user_type, username)
        #     return queryset


# class ListParentStudent(generics.ListCreateAPIView):
#     serializer_class = TeacherSerializer
#
#     def get_queryset(self):
#         queryset = Student.objects.all()
#         user_type = self.request.user.user_type
#         username = self.request.query_params.get('username', None)
#         ############## Get My Children #######################
#         if username is not None and user_type == "parent":
#             queryset = queryset.filter(parent__username=username)
#             print(user_type, username)
#             return queryset




























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
    # filter_backends = (filters.DjangoFilterBackend,)

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




# ############### Parent info ##################
# class MyStudents(generics.ListCreateAPIView):
#     serializer_class = ParentSerializer
#     def get_queryset(self):
#         queryset = Student.objects.all()
#         username = self.request.query_params.get('username', None)
#         if username is not None:
#             queryset = queryset.filter(username=username)
#         return queryset
