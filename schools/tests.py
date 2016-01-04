from django.test import TestCase, Client
from django.core.urlresolvers import reverse
# Create your tests here.
from parents.models import Parent
from schools.models import *
from teachers.models import Teacher
from rest_framework import status
from schools.views import *
from rest_framework.test import APITestCase, APIRequestFactory
from datetime import date

#################### PARENT VIEWS TESTS #################################
class ParentTests(TestCase):

    def setUp(self):
        self.parent = Parent.objects.create(username='bob', email='bob@bob.com', password='password' ,first_name="bob")
        self.student1 = Student.objects.create(first_name='bobby', last_name='hill',)
        self.student1.parent.add(self.parent)
        self.student2 = Student.objects.create(first_name='peggy', last_name='hill',)
        self.student2.parent.add(self.parent)

    def test_parent_list(self):
        url = reverse('parent_list')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_parent = response.data['results'][0]
        self.assertEqual(response_parent['first_name'], self.parent.first_name)

    def test_parent_list_request(self):
        url = reverse('parent_list')
        view = ParentList.as_view()
        factory = APIRequestFactory()
        request = factory.get(url, {}, format='json')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_parent = response.data['results'][0]
        self.assertEqual(response_parent['first_name'], self.parent.first_name)

    def test_parent_detail(self):
        url = reverse('parent_detail', args=(self.parent.id,))
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_parent = response.data
        self.assertEqual(response_parent['first_name'], self.parent.first_name)
        self.assertEqual(response_parent['id'], self.parent.id)

    def test_parent_student_list(self):
        url = reverse('parent_student_list', args=(self.parent.id,))
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)
        response_student = response.data['results'][0]
        self.assertEqual(response_student['first_name'], self.student1.first_name)

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

    def test_teacher_list_request(self):
        url = reverse('teacher_list')
        view = ListTeachers.as_view()
        factory = APIRequestFactory()
        request = factory.get(url, {}, format='json')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_teacher = response.data['results'][0]
        self.assertEqual(response_teacher['first_name'], self.teacher.first_name)


#################### STUDENT VIEWS TESTS #################################
class StudentTests(TestCase):

    def setUp(self):
        self.student = Student.objects.create(first_name='bobby', last_name='hill',)

    def test_student_list(self):
        url = reverse('student_list')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_student = response.data['results'][0]
        self.assertEqual(response_student['first_name'], self.student.first_name)

    def test_student_list_request(self):
        url = reverse('student_list')
        view = ListStudents.as_view()
        factory = APIRequestFactory()
        request = factory.get(url, {}, format='json')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_student = response.data['results'][0]
        self.assertEqual(response_student['first_name'], self.student.first_name)


#################### SCHOOL_CLASS VIEWS TESTS #################################
class SchoolClassTests(TestCase):

    def setUp(self):
        self.school = School.objects.create(name="iron yard")
        self.teacher = Teacher.objects.create(username='bob', email='bob@bob.com', password='password')
        self.school_class = SchoolClass.objects.create(name='python', teacher=self.teacher, school=self.school)

    def test_school_class_list(self):
        url = reverse('school_class_list')
        view = ListClasses.as_view()
        factory = APIRequestFactory()
        request = factory.get(url, {}, format='json')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_school_class = response.data['results'][0]
        self.assertEqual(response_school_class['name'], self.school_class.name)
        self.assertEqual(response_school_class['teacher'], self.school_class.teacher.id)
        self.assertEqual(response_school_class['school'], self.school_class.school.id)

    def test_school_class_list_request(self):
        url = reverse('school_class_list')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_school_class = response.data['results'][0]
        self.assertEqual(response_school_class['name'], self.school_class.name)
        self.assertEqual(response_school_class['teacher'], self.school_class.teacher.id)
        self.assertEqual(response_school_class['school'], self.school_class.school.id)


#################### SCHOOL VIEWS TESTS #################################
class SchoolTests(TestCase):

    def setUp(self):
        self.school = School.objects.create(name="iron yard")

    def test_school_list(self):
        url = reverse('school_list')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_school = response.data['results'][0]
        self.assertEqual(response_school['name'], self.school.name)

    def test_school_list_request(self):
        url = reverse('school_list')
        view = ListSchools.as_view()
        factory = APIRequestFactory()
        request = factory.get(url, {}, format='json')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_school = response.data['results'][0]
        self.assertEqual(response_school['name'], self.school.name)



#################  SCHOOL EVENTS #####################
class SchoolEventTests(TestCase):

    def setUp(self):
        self.school = School.objects.create(name="iron yard")
        self.school_event = SchoolEvent.objects.create(name='field day', school=self.school,description="will be fun!",)

    def test_school_event_list(self):
        url = reverse('school_event_list')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_school_event = response.data['results'][0]
        self.assertEqual(response_school_event['name'], self.school_event.name)

    def test_school_event_list_request(self):
        url = reverse('school_event_list')
        view = ListSchoolEvents.as_view()
        factory = APIRequestFactory()
        request = factory.get(url, {}, format='json')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_school_event = response.data['results'][0]
        self.assertEqual(response_school_event['name'], self.school_event.name)

#################  CLASS EVENTS #####################
class ClassEventTests(TestCase):

    def setUp(self):
        self.school = School.objects.create(name="iron yard")
        self.teacher = Teacher.objects.create(username='bob', email='bob@bob.com', password='password')
        self.school_class = SchoolClass.objects.create(name='python', teacher=self.teacher, school=self.school)
        self.class_event = ClassEvent.objects.create(name='field day', school_class=self.school_class)

    def test_class_event_list(self):
        url = reverse('class_event_list')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_class_event = response.data['results'][0]
        self.assertEqual(response_class_event['name'], self.class_event.name)

    def test_class_event_list_request(self):
        url = reverse('class_event_list')
        view = ListClassEvents.as_view()
        factory = APIRequestFactory()
        request = factory.get(url, {}, format='json')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_class_event = response.data['results'][0]
        self.assertEqual(response_class_event['name'], self.class_event.name)

#################  CLASS FEES #####################
class ClassFeeTests(TestCase):
    def setUp(self):
        self.school = School.objects.create(name="iron yard")
        self.teacher = Teacher.objects.create(username='bob', email='bob@bob.com', password='password')
        self.school_class = SchoolClass.objects.create(name='python', teacher=self.teacher, school=self.school)
        self.student = Student.objects.create(first_name='bobby', last_name='hill',)
        self.class_fee = ClassFee.objects.create(school_class=self.school_class, name='field day fee',
                                                 description="neccesary cost", amount=10)
        self.class_fee_payment = ClassFeePayment.objects.create(student=self.student,
                                                                class_fee=self.class_fee,
                                                                name=self.class_fee.name)

    def test_class_fee_list(self):
            url = reverse('class_fee_list')
            response = self.client.get(url, {}, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data['count'], 1)
            response_class_fee = response.data['results'][0]
            self.assertEqual(response_class_fee['name'], self.class_fee.name)

###############   HOMEWORK  #################

#################  FORMS #####################

#################  ATTENDANCE #####################


#################  BEHAVIOR #####################
