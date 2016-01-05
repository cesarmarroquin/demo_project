from schools.views import *
from django.conf.urls import url, include
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    ###############   TOKEN ENDPOINT USED FOR LOGIN AND USER AUTHENTICATION #################
    url(r'^api-token-auth/', ObtainAuthToken3.as_view()),

    ###############   RETRIEVE USERS BASIC INFORMATION #################
    url(r'^my_info/$', MyInfo.as_view(), name='my_info'),

    ###############   PARENT ENDPOINTS #################
    url(r'^parents/$', ParentList.as_view(), name='parent_list'),
    url(r'^parents/(?P<pk>\d+)$', ParentDetail.as_view(), name='parent_detail'),
    url(r'^parents/(?P<pk>\d+)/students$', ParentStudentsList.as_view(), name='parent_student_list'),

    ###############   TEACHER ENDPOINTS #################
    url(r'^teachers/$', ListTeachers.as_view(), name='teacher_list'),
    url(r'^teachers/(?P<pk>\d+)$', DetailTeachers.as_view(), name='teacher_detail'),
    url(r'^teachers/(?P<pk>\d+)/classes$', TeacherClassList.as_view(), name='teacher_class_list'),

    ###############   STUDENT ENDPOINTS #################
    url(r'^students/$', ListStudents.as_view(), name='student_list'),
    url(r'^students/(?P<pk>\d+)$', DetailStudents.as_view(), name='student_detail'),
    url(r'^students/(?P<pk>\d+)/fees$', StudentFeeList.as_view(), name='student_fee_list'),
    url(r'^students/(?P<pk>\d+)/homework$', StudentHomeworkList.as_view(), name='student_homework_list'),
    url(r'^students/(?P<pk>\d+)/forms$', StudentFormList.as_view(), name='student_form_list'),
    url(r'^students/(?P<pk>\d+)/attendance$', StudentAttendanceList.as_view(), name='student_attendance_list'),
    url(r'^students/(?P<pk>\d+)/behavior$', StudentBehaviorList.as_view(), name='student_behavior_list'),

    ###############   CLASS ENDPOINTS #################
    url(r'^classes/$', ListClasses.as_view(), name='school_class_list'),
    url(r'^classes/(?P<pk>\d+)$', DetailClasses.as_view(), name='school_class_detail'),
    url(r'^classes/(?P<pk>\d+)/events$', ClassEventList.as_view(), name='school_class_class_event_list'),
    url(r'^classes/(?P<pk>\d+)/fees$', ClassFeeList.as_view(), name='school_class_class_fee_list'),
    url(r'^classes/(?P<pk>\d+)/students$', ClassStudentList.as_view(), name='school_class_student_list'),

    ###############   SCHOOL ENDPOINTS #################
    url(r'^schools/$', ListSchools.as_view(), name='school_list'),
    url(r'^schools/(?P<pk>\d+)$', DetailSchools.as_view(), name='school_detail'),
    url(r'^schools/(?P<pk>\d+)/classes$', SchoolClassList.as_view(), name='school_school_class_list'),
    url(r'^schools/(?P<pk>\d+)/events$', SchoolEventList.as_view(), name='school_school_event_list'),

    ###############   SCHOOL EVENT ENDPOINTS #################
    url(r'^school_events/$', ListSchoolEvents.as_view(), name='school_event_list'),
    url(r'^school_events/(?P<pk>\d+)$', DetailSchoolEvents.as_view(), name='school_event_detail'),

    ###############   CLASS EVENT ENDPOINTS #################
    url(r'^class_events/$', ListClassEvents.as_view(), name='school_class_event_list'),
    url(r'^class_events/(?P<pk>\d+)$', DetailClassEvents.as_view(), name='school_class_event_detail'),

    ###############   CLASS FEE ENDPOINTS #################
    url(r'^class_fees/$', ListClassFees.as_view(), name='school_class_fee_list'),
    url(r'^class_fees/(?P<pk>\d+)$', DetailClassFees.as_view(), name='school_class_fee_detail'),

    ###############   HOMEWORK ENDPOINTS #################
    url(r'^student_homework/(?P<pk>\d+)$', DetailStudentHomework.as_view(), name='detail_class_fees'),

    ###############   FORM ENDPOINTS #################
    url(r'^student_forms/$', ListStudentForms.as_view(), name='detail_class_fees'),
    url(r'^student_forms/(?P<pk>\d+)$', DetailStudentForms.as_view(), name='detail_class_fees'),

    ###############  ATTENDANCE ENDPOINTS #################
    url(r'^student_attendance/$', ListStudentAttendance.as_view(), name='detail_class_fees'),
    url(r'^student_attendance/(?P<pk>\d+)$', DetailStudentAttendance.as_view(), name='detail_class_fees'),

    ###############  BEHAVIOR ENDPOINTS #################
    url(r'^student_behavior/$', ListStudentBehavior.as_view(), name='detail_class_fees'),
    url(r'^student_behavior/(?P<pk>\d+)$', DetailStudentBehavior.as_view(), name='detail_class_fees'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
