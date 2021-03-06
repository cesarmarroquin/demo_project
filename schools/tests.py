from django.test import TestCase, Client
from django.core.urlresolvers import reverse
# Create your tests here.
from parents.models import Parent
from schools.models import *
from teachers.models import Teacher
from rest_framework import status
from schools.views import *
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from datetime import date


###### AUTH TOKEN TEST ###################
class AuthTest(APITestCase):
    def test_ObtainAuthToken3(self):
        self.client = APIClient()
        self.url = reverse("token_auth")
        self.parent = Parent.objects.create(username='maria', email='maria@maria.com', password='123' ,first_name="maria")
        get = self.client.get(self.url, {}, format='json')
        post = self.client.post(self.url, {"username": self.parent.username, "password": self.parent.password}, format='json')
        self.assertEqual(get.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        print(post.content)

        # print(view(post))

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
        self.student1.school_class.add(self.school_class2)
        self.student1.save()
        self.student2 = Student.objects.create(first_name='peggy', last_name='hill',)
        self.student2.parent.add(self.parent)
        self.student3 = Student.objects.create(first_name='bart', last_name='simpson',)
        self.class_fee = ClassFee.objects.create(school_class=self.school_class1,name="art fee",description="fee for paint",amount=10)
        self.fee_payment1 = ClassFeePayment.objects.create(student=self.student1, class_fee = self.class_fee)
        self.class_homework = ClassHomework.objects.create(school_class=self.school_class1,title="math hw", description="addition", points=10)
        self.homework1 = StudentHomework.objects.create(class_homework=self.class_homework,student=self.student1)
        self.attendance1 = StudentAttendance.objects.create(school_class=self.school_class1,student=self.student1)
        self.behavior1 = StudentBehavior.objects.create(school_class=self.school_class1,student=self.student1)
        self.class_event1 = ClassEvent.objects.create(school_class=self.school_class1,name="field trip")
        self.school_event1 = SchoolEvent.objects.create(school=self.school,name="field trip")


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
        # print(url)
        response = self.client.get(url, {}, format='json')
        # print(response.data)
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

    def test_student_attendance_list(self):
        response = self.nested_resource_list_response('student_attendance_list',self.student1,len(StudentAttendance.objects.filter(student__id = self.student1.id)))
        self.nested_resource_list_shared_tests(response, self.attendance1,)
        self.assertEqual(response.data['count'], len(StudentAttendance.objects.filter(student__id = self.student1.id)))

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
        response = self.nested_resource_list_response('school_class_class_event_list',self.school_class1, 1)
        self.nested_resource_list_shared_tests(response, self.class_event1,)
        self.assertEqual(response.data['count'], len(ClassEvent.objects.filter(school_class__id = self.school_class1.id)))

    def test_school_class_fee_list(self):
        response = self.nested_resource_list_response('school_class_class_fee_list',self.school_class1,1)
        self.nested_resource_list_shared_tests(response, self.class_fee,)
        self.assertEqual(response.data['count'], len(ClassFee.objects.filter(school_class__id = self.school_class1.id)))
    # #
    def test_school_class_student_list(self):
        response = self.nested_resource_list_response('school_class_student_list',self.school_class2,1)
        self.nested_resource_list_shared_tests(response, self.student1,)
        self.assertEqual(response.data['count'], len(Student.objects.filter(school_class__id = self.school_class2.id)))



#################### SCHOOL VIEWS TESTS #################################
class SchoolTests(BaseApiTestClass):

    def test_school_list(self):
        response = self.list_response('school_list')
        self.list_shared_tests(response, School, self.school)

    def test_school_detail(self):
        response = self.detail_response('school_detail',self.school)
        self.detail_shared_tests(response, self.school)

    def test_school_class_list(self):
        response = self.nested_resource_list_response('school_school_class_list',self.school,1)
        self.nested_resource_list_shared_tests(response, self.school_class2,)
        self.assertEqual(response.data['count'], len(SchoolClass.objects.filter(school__id = self.school.id)))

    def test_school_event_list(self):
        response = self.nested_resource_list_response('school_school_event_list',self.school,1)
        self.nested_resource_list_shared_tests(response, self.school_event1,)
        self.assertEqual(response.data['count'], len(SchoolEvent.objects.filter(school__id = self.school.id)))


#
# #################  SCHOOL EVENTS #####################
class SchoolEventTests(BaseApiTestClass):

    def test_school_eventlist(self):
        response = self.list_response('school_event_list')
        self.list_shared_tests(response, SchoolEvent, self.school)

    def test_school_eventdetail(self):
        response = self.detail_response('school_event_detail',self.school)
        self.detail_shared_tests(response, self.school_event1)


##################  CLASS EVENTS #####################
class SchoolClassEventTests(BaseApiTestClass):

    def test_school_class_event_list(self):
        response = self.list_response('school_class_event_list')
        self.list_shared_tests(response, ClassEvent, self.class_event1)

    def test_school_class_event_detail(self):
        response = self.detail_response('school_class_event_detail',self.class_event1)
        self.detail_shared_tests(response, self.class_event1)


##################  CLASS FEES #####################
class SchoolClassFeeTests(BaseApiTestClass):

    def test_school_class_fee_list(self):
        response = self.list_response('school_class_fee_list')
        self.list_shared_tests(response, ClassFee, self.class_fee)

    def test_school_class_fee_detail(self):
        response = self.detail_response('school_class_fee_detail',self.class_fee)
        self.detail_shared_tests(response, self.class_fee)



# ###############   HOMEWORK  #################
class SchoolStudentHomeworkTests(BaseApiTestClass):

    def test_homework_list(self):
        response = self.list_response('homework_list')
        self.list_shared_tests(response, StudentHomework, self.homework1)

    def test_homework_detail(self):
        response = self.detail_response('homework_detail',self.homework1)
        self.detail_shared_tests(response, self.homework1)


# #################  ATTENDANCE #####################
class AttendanceTests(BaseApiTestClass):

    def test_attendance_list(self):
        response = self.list_response('attendance_list')
        self.list_shared_tests(response, StudentAttendance, self.attendance1)

    def test_attendance_detail(self):
        response = self.detail_response('attendance_detail',self.attendance1)
        self.detail_shared_tests(response, self.attendance1)
# #################  BEHAVIOR #####################
class BehaviorTests(BaseApiTestClass):

    def test_behavior_list(self):
        response = self.list_response('behavior_list')
        self.list_shared_tests(response, StudentBehavior, self.behavior1)

    def test_behavior_detail(self):
        response = self.detail_response('behavior_detail',self.behavior1)
        self.detail_shared_tests(response, self.behavior1)