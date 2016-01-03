from django.test import TestCase, Client
from django.core.urlresolvers import reverse
# Create your tests here.
from parents.models import Parent
from schools.models import *
from teachers.models import Teacher
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory


class ParentTests(TestCase):

    def setUp(self):
        self.school = School.objects.create(name="iron yard")
        self.teacher = Teacher.objects.create('jeff', 'jeff@jeff.com', password='123')
        self.user = Parent.objects.create_user('bob', 'bob@bob.com', password='password')
        self.school_class = SchoolClass.objects.create(name = "python backend", teacher = self.teacher, school= self.school)
        self.student = Student.objects.create(first_name="cesar", last_name="marroquin", parent=self.user)

    def test_parent_student_list(self):
        url = reverse('list_parents')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_student = response.data['results'][0]
        self.assertEqual(response_student['name'], self.student.first_name)


class TeacherTests(TestCase):

    def setUp(self):
        self.school = School.objects.create(name="iron yard")
        self.teacher = Teacher.objects.create('jeff', 'jeff@jeff.com', password='123')
        self.user = Parent.objects.create_user('bob', 'bob@bob.com', password='password')
        self.school_class = SchoolClass.objects.create(name = "python backend", teacher = self.teacher, school= self.school)
        self.student = Student.objects.create(first_name="cesar", last_name="marroquin", parent=self.user)

    def test_parent_student_list(self):
        url = reverse('list_teachers')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_teacher = response.data['results'][0]
        self.assertEqual(response_teacher['name'], self.teacher.first_name)
        self.assertEqual(response_teacher['user_type'], 'teacher')


class SchoolClassTests(TestCase):
    def setUp(self):
        self.school = School.objects.create(name="iron yard")
        self.teacher = Teacher.objects.create('jeff', 'jeff@jeff.com', password='123')
        self.user = Parent.objects.create_user('bob', 'bob@bob.com', password='password')
        self.school_class = SchoolClass.objects.create(name = "python backend", teacher = self.teacher, school= self.school)
        self.student = Student.objects.create(first_name="cesar", last_name="marroquin", parent=self.user)

    def test_parent_student_list(self):
        url = reverse('list_classes')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)