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
class BaseApiTestClass(APITestCase):
    def setUp(self):
        self.parent = Parent.objects.create(username='maria', email='maria@maria.com', password='123' ,first_name="maria")
        self.teacher = self.teacher = Teacher.objects.create(username='jeff', email='jeff@jeff.com', password='123')
        self.student1 = Student.objects.create(first_name='cesar', last_name='marroquin',)
        self.student1.parent.add(self.parent)
        self.student2 = Student.objects.create(first_name='peggy', last_name='hill',)
        self.student2.parent.add(self.parent)
        self.school = School.objects.create(name="iron yard")
        self.school_class1 = SchoolClass.objects.create(name='back-end', teacher=self.teacher, school=self.school)
        self.school_class2 = SchoolClass.objects.create(name='front-end', teacher=self.teacher, school=self.school)

    def list_test_setup(self, url_name,):
        url = reverse(url_name)
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response = response.data['results'][0]
        return response

    def detail_test_setup(self,url_name,model_name):
        url = reverse(url_name, args=(model_name.id,))
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = response.data
        return response

    def nested_resource_list_test_setup(self,url_name,model_name,data_count):
        url = reverse(url_name,args=(model_name.id,))
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], data_count)
        response = response.data['results'][0]
        return response

    # def assert_equal_tests(self,response_name,model_name,field_name):
    # def
class ParentTests(BaseApiTestClass):
    def test_parent_list(self):
        response = self.list_test_setup('parent_list')
        self.assertEqual(response['first_name'], self.parent.first_name)

    def test_parent_detail(self):
        response = self.detail_test_setup('parent_detail',self.parent)
        self.assertEqual(response['first_name'], self.parent.first_name)
        self.assertEqual(response['id'], self.parent.id)

    def test_parent_student_list(self):
        response = self.nested_resource_list_test_setup('parent_student_list',self.parent,2)
        self.assertEqual(response['first_name'], self.student1.first_name)

#################### TEACHER VIEWS TESTS #################################
class TeacherTests(BaseApiTestClass):
    def test_parent_list(self):
        response = self.list_test_setup('teacher_list')
        self.assertEqual(response['first_name'], self.teacher.first_name)

    def test_teacher_detail(self):
        response = self.detail_test_setup('teacher_detail',self.teacher)
        self.assertEqual(response['first_name'], self.teacher.first_name)
        self.assertEqual(response['id'], self.teacher.id)

    def test_teacher_class_list(self):
        response = self.nested_resource_list_test_setup('teacher_class_list',self.teacher,2)
        self.assertEqual(response['name'], self.school_class2.name)

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


    def test_student_detail(self):
        url = reverse('student_detail', args=(self.student.id,))
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_student = response.data
        self.assertEqual(response_student['first_name'], self.student.first_name)
        self.assertEqual(response_student['id'], self.student.id)

    # def test_student_fees(self):
    #
    # def test_student_homework(self):
    #
    # def test_student_forms(self):
    #
    # def test_student_attendance(self):
    #
    # def test_student_behavior(self):


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
