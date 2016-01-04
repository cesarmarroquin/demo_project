from django.test import TestCase, Client
from django.core.urlresolvers import reverse
# Create your tests here.
from parents.models import Parent
from schools.models import *
from teachers.models import Teacher
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

#################### PARENT VIEWS TESTS #################################
class ParentTests(TestCase):

    def setUp(self):
        # self.school = School.objects.create(name="iron yard")
        # self.teacher = Teacher.objects.create(username='jeff', email='jeff@jeff.com', password='123')
        # self.user = Parent.objects.create(username='bob', email='bob@bob.com', password='password')
        # self.school_class = SchoolClass.objects.create(name = "python backend", teacher = self.teacher, school= self.school)
        # # self.student = Student.objects.create(first_name="cesar", last_name="marroquin", parent=self.user)
        self.parent = Parent.objects.create(username='bob', email='bob@bob.com', password='password' ,first_name="bob")

    def test_parent_list(self):

        url = reverse('parent_list')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_parent = response.data['results'][0]
        self.assertEqual(response_parent['first_name'], self.parent.first_name)

#################### TEACHER VIEWS TESTS #################################
class TeacherTests(TestCase):

    def setUp(self):
        self.teacher = Teacher.objects.create(username='bob', email='bob@bob.com', password='password')

    def test_teacher_list(self):
        url = reverse('teacher_list')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_teacher = response.data['results'][0]
        self.assertEqual(response_teacher['first_name'], self.teacher.first_name)


#################### STUDENT VIEWS TESTS #################################


#################### SCHOOL_CLASS VIEWS TESTS #################################



#################### SCHOOL VIEWS TESTS #################################



#################  SCHOOL EVENTS #####################

#################  CLASS EVENTS #####################


#################  CLASS FEES #####################


#################  FORMS #####################

#################  ATTENDANCE #####################


#################  BEHAVIOR #####################








