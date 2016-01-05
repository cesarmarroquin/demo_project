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
        self.teacher = Teacher.objects.create(username='jeff', email='jeff@jeff.com', password='123')
        self.school = School.objects.create(name="iron yard")
        self.school_class1 = SchoolClass.objects.create(name='back-end', teacher=self.teacher, school=self.school)

        self.school_class2 = SchoolClass.objects.create(name='front-end', teacher=self.teacher, school=self.school)


        self.student1 = Student.objects.create(first_name='cesar', last_name='marroquin',)
        self.student1.parent.add(self.parent)


        self.student2 = Student.objects.create(first_name='peggy', last_name='hill',)
        self.student2.parent.add(self.parent)
        self.student3 = Student.objects.create(first_name='bart', last_name='simpson',)


        self.class_fee = ClassFee.objects.create(school_class=self.school_class1,name="art fee",description="fee for paint",amount=10)
        self.fee_payment1 = ClassFeePayment.objects.create(student=self.student1, class_fee = self.class_fee)
        self.class_homework = ClassHomework.objects.create(school_class=self.school_class1,title="math hw", description="addition", points=10)
        self.homework1 = StudentHomework.objects.create(class_homework=self.class_homework,student=self.student1)
        # self.class_form = ClassForm.objects.create(school_class=self.school_class1,)
        # self.student_form1 = StudentForm.objects.create(class_form=self.class_form, student=self.student1, signer=self.parent, file=)
        self.attendance1 = StudentAttendance.objects.create(school_class=self.school_class1,student=self.student1)
        self.behavior1 = StudentBehavior.objects.create(school_class=self.school_class1,student=self.student1)
        self.class_event1 = ClassEvent.objects.create(school_class=self.school_class1,name="field trip")


    def list_response(self, url_name,):
        url = reverse(url_name)
        response = self.client.get(url, {}, format='json')
        return response

    def detail_response(self,url_name,model_name):
        url = reverse(url_name, args=(model_name.id,))
        response = self.client.get(url, {}, format='json')
        return response

    def nested_resource_list_response(self,url_name,model_name,data_count):
        url = reverse(url_name,args=(model_name.id,))
        response = self.client.get(url, {}, format='json')
        return response

    def list_shared_tests(self, response_name, model_name, model_instance):
        self.assertEqual(response_name.status_code, status.HTTP_200_OK)
        self.assertEqual(response_name.data['results'][0]['id'], model_instance.id)
        self.assertEqual(response_name.data['count'], len(model_name.objects.all()))


    def detail_shared_tests(self, response_name, model_instance):
        self.assertEqual(response_name.status_code, status.HTTP_200_OK)
        self.assertEqual(response_name.data['id'], model_instance.id)

    def nested_resource_list_shared_tests(self, response_name, resource_instance,):
        self.assertEqual(response_name.status_code, status.HTTP_200_OK)
        self.assertEqual(response_name.data['results'][0]['id'], resource_instance.id)




#################### PARENT VIEWS TESTS #################################
class ParentTests(BaseApiTestClass):
    def test_parent_list(self):
        response = self.list_response('parent_list')
        self.list_shared_tests(response, Parent, self.parent)

    def test_parent_detail(self):
        response = self.detail_response('parent_detail',self.parent)
        self.detail_shared_tests(response, self.parent)

    def test_parent_student_list(self):
        response = self.nested_resource_list_response('parent_student_list',self.parent,2)
        self.nested_resource_list_shared_tests(response, self.student1,)
        self.assertEqual(response.data['count'], len(Student.objects.filter(parent__id=self.parent.id)))


#################### Teacher VIEWS TESTS #################################
class TeacherTests(BaseApiTestClass):
    def test_teacher_list(self):
        response = self.list_response('teacher_list')
        self.list_shared_tests(response, Teacher, self.teacher)

    def test_teacher_detail(self):
        response = self.detail_response('teacher_detail',self.teacher)
        self.detail_shared_tests(response, self.teacher)

    def test_teacher_student_list(self):
        response = self.nested_resource_list_response('teacher_class_list',self.teacher,2)
        self.nested_resource_list_shared_tests(response, self.school_class2,)
        self.assertEqual(response.data['count'], len(SchoolClass.objects.filter(teacher__id=self.teacher.id)))


#################### STUDENT VIEWS TESTS #################################
class StudentTests(BaseApiTestClass):
    def test_student_list(self):
        response = self.list_response('student_list')
        self.list_shared_tests(response, Student, self.student1)

    def test_student_detail(self):
        response = self.detail_response('student_detail',self.student1)
        self.detail_shared_tests(response, self.student1)

    def test_student_fee_list(self):
        response = self.nested_resource_list_response('student_fee_list',self.student1,len(ClassFeePayment.objects.filter(student__id = self.student1.id)))
        self.nested_resource_list_shared_tests(response, self.fee_payment1,)
        self.assertEqual(response.data['count'], len(ClassFeePayment.objects.filter(student__id = self.student1.id)))

    def test_student_homework_list(self):
        response = self.nested_resource_list_response('student_homework_list',self.student1,len(StudentHomework.objects.filter(student__id = self.student1.id)))
        self.nested_resource_list_shared_tests(response, self.homework1,)
        self.assertEqual(response.data['count'], len(StudentHomework.objects.filter(student__id = self.student1.id)))

#     def test_student_form_list(self):
#         response = self.nested_resource_list_response('student_form_list',self.student1,len(StudentForm.objects.filter(student__id = self.student1.id)))
#         self.nested_resource_list_shared_tests(response, self.form1,)
#         self.assertEqual(response.data['count'], len(StudentForm.objects.filter(student__id = self.student1.id)))
# #
    def test_student_attendance_list(self):
        response = self.nested_resource_list_response('student_attendance_list',self.student1,len(StudentAttendance.objects.filter(student__id = self.student1.id)))
        self.nested_resource_list_shared_tests(response, self.attendance1,)
        self.assertEqual(response.data['count'], len(StudentAttendance.objects.filter(student__id = self.student1.id)))
#
    def test_student_behavior_list(self):
        response = self.nested_resource_list_response('student_behavior_list',self.student1,len(StudentBehavior.objects.filter(student__id = self.student1.id)))
        self.nested_resource_list_shared_tests(response, self.behavior1,)
        self.assertEqual(response.data['count'], len(StudentBehavior.objects.filter(student__id = self.student1.id)))



    #################### SCHOOL_CLASS VIEWS TESTS #################################
class SchoolClassTests(BaseApiTestClass):

    def test_school_class_list(self):
        response = self.list_response('school_class_list')
        self.list_shared_tests(response, SchoolClass, self.school_class1)

    def test_school_class_detail(self):
        response = self.detail_response('school_class_detail',self.school_class1)
        self.detail_shared_tests(response, self.school_class1)

    def test_school_class_event_list(self):
        response = self.nested_resource_list_response('school_class_fee_list',self.school_class1,len(ClassEvent.objects.filter(school_class__id = self.school_class1.id)))
        self.nested_resource_list_shared_tests(response, self.class_event1,)
        self.assertEqual(response.data['count'], len(ClassEvent.objects.filter(school_class__id = self.school_class1.id)))

    def test_school_class_fee_list(self):
        response = self.nested_resource_list_response('school_class_fee_list',self.school_class1,len(ClassFee.objects.filter(school_class__id = self.school_class1.id)))
        self.nested_resource_list_shared_tests(response, self.class_fee,)
        self.assertEqual(response.data['count'], len(ClassFee.objects.filter(school_class__id = self.school_class1.id)))
    #
    def test_school_class_student_list(self):
        response = self.nested_resource_list_response('school_class_student_list',self.school_class1,len(Student.objects.filter(school_class__id = self.school_class1.id)))
        self.nested_resource_list_shared_tests(response, self.student2,)
        self.assertEqual(response.data['count'], len(Student.objects.filter(school_class__id = self.school_class1.id)))



#################### SCHOOL_CLASS VIEWS TESTS #################################
class SchoolTests(BaseApiTestClass):

    def test_school_list(self):
        response = self.list_response('school_list')
        self.list_shared_tests(response, School, self.school)

    def test_school_detail(self):
        response = self.detail_response('school_detail',self.school)
        self.detail_shared_tests(response, self.school)






# #################### TEACHER VIEWS TESTS #################################
# class TeacherTests(BaseApiTestClass):
#     def test_parent_list(self):
#         response = self.list_test_setup('teacher_list')
#         self.assertEqual(response['first_name'], self.teacher.first_name)
#
#     def test_teacher_detail(self):
#         response = self.detail_test_setup('teacher_detail',self.teacher)
#         self.assertEqual(response['first_name'], self.teacher.first_name)
#         self.assertEqual(response['id'], self.teacher.id)
#
#     def test_teacher_class_list(self):
#         response = self.nested_resource_list_test_setup('teacher_class_list',self.teacher,2)
#         self.assertEqual(response['name'], self.school_class2.name)
#
# #################### STUDENT VIEWS TESTS #################################
# class StudentTests(TestCase):
#
#     def setUp(self):
#         self.student = Student.objects.create(first_name='bobby', last_name='hill',)
#
#     def test_student_list(self):
#         url = reverse('student_list')
#         response = self.client.get(url, {}, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['count'], 1)
#         response_student = response.data['results'][0]
#         self.assertEqual(response_student['first_name'], self.student.first_name)
#
#
#     def test_student_detail(self):
#         url = reverse('student_detail', args=(self.student.id,))
#         response = self.client.get(url, {}, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         response_student = response.data
#         self.assertEqual(response_student['first_name'], self.student.first_name)
#         self.assertEqual(response_student['id'], self.student.id)
#
#     # def test_student_fees(self):
#     #
#     # def test_student_homework(self):
#     #
#     # def test_student_forms(self):
#     #
#     # def test_student_attendance(self):
#     #
#     # def test_student_behavior(self):
#
#

#
#
#
# #################### SCHOOL VIEWS TESTS #################################
# class SchoolTests(TestCase):
#
#     def setUp(self):
#         self.school = School.objects.create(name="iron yard")
#
#     def test_school_list(self):
#         url = reverse('school_list')
#         response = self.client.get(url, {}, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['count'], 1)
#         response_school = response.data['results'][0]
#         self.assertEqual(response_school['name'], self.school.name)
#
#
#
#
# #################  SCHOOL EVENTS #####################
# class SchoolEventTests(TestCase):
#
#     def setUp(self):
#         self.school = School.objects.create(name="iron yard")
#         self.school_event = SchoolEvent.objects.create(name='field day', school=self.school,description="will be fun!",)
#
#     def test_school_event_list(self):
#         url = reverse('school_event_list')
#         response = self.client.get(url, {}, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['count'], 1)
#         response_school_event = response.data['results'][0]
#         self.assertEqual(response_school_event['name'], self.school_event.name)
#
#
# #################  CLASS EVENTS #####################
# class ClassEventTests(TestCase):
#
#     def setUp(self):
#         self.school = School.objects.create(name="iron yard")
#         self.teacher = Teacher.objects.create(username='bob', email='bob@bob.com', password='password')
#         self.school_class = SchoolClass.objects.create(name='python', teacher=self.teacher, school=self.school)
#         self.class_event = ClassEvent.objects.create(name='field day', school_class=self.school_class)
#
#     def test_class_event_list(self):
#         url = reverse('class_event_list')
#         response = self.client.get(url, {}, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['count'], 1)
#         response_class_event = response.data['results'][0]
#         self.assertEqual(response_class_event['name'], self.class_event.name)
#
#
# #################  CLASS FEES #####################
# class ClassFeeTests(TestCase):
#     def setUp(self):
#         self.school = School.objects.create(name="iron yard")
#         self.teacher = Teacher.objects.create(username='bob', email='bob@bob.com', password='password')
#         self.school_class = SchoolClass.objects.create(name='python', teacher=self.teacher, school=self.school)
#         self.student = Student.objects.create(first_name='bobby', last_name='hill',)
#         self.class_fee = ClassFee.objects.create(school_class=self.school_class, name='field day fee',
#                                                  description="neccesary cost", amount=10)
#         self.class_fee_payment = ClassFeePayment.objects.create(student=self.student,
#                                                                 class_fee=self.class_fee,
#                                                                 name=self.class_fee.name)
#
#     def test_class_fee_list(self):
#             url = reverse('class_fee_list')
#             response = self.client.get(url, {}, format='json')
#             self.assertEqual(response.status_code, status.HTTP_200_OK)
#             self.assertEqual(response.data['count'], 1)
#             response_class_fee = response.data['results'][0]
#             self.assertEqual(response_class_fee['name'], self.class_fee.name)
#
# ###############   HOMEWORK  #################
#
# #################  FORMS #####################
#
# #################  ATTENDANCE #####################
#
#
# #################  BEHAVIOR #####################