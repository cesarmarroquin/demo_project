from api.views import *
from django.conf.urls import url, include
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    ###############   TOKEN ENDPOINT USED FOR LOGIN AND USER AUTHENTICATION #################
    url(r'^api-token-auth/', ObtainAuthToken2.as_view()),

    ###############   RETRIEVE USERS BASIC INFORMATION #################
    url(r'^my_info/$', MyInfo.as_view(), name='my_info'),

    ###############   PARENT ENDPOINTS #################
    url(r'^parents/$', ParentList.as_view(), name='parent_list'),
    url(r'^parents/(?P<pk>\d+)$', ParentDetail.as_view(), name='parent_detail'),
    url(r'^parents/(?P<pk>\d+)/students$', ParentStudentsList.as_view(), name='parent_detail'),

    ###############   TEACHER ENDPOINTS #################
    url(r'^teachers/$', ListTeachers.as_view(), name='list_teachers'),
    url(r'^teachers/(?P<pk>\d+)$', DetailTeachers.as_view(), name='detail_teachers'),
    url(r'^teachers/(?P<pk>\d+)/classes$', TeacherClassList.as_view(), name='detail_teachers'),

    ###############   STUDENT ENDPOINTS #################
    url(r'^students/$', ListStudents.as_view(), name='list_students'),
    url(r'^students/(?P<pk>\d+)$', DetailStudents.as_view(), name='detail_students'),
    url(r'^students/(?P<pk>\d+)/fees$', StudentFeeList.as_view(), name='detail_students'),
    url(r'^students/(?P<pk>\d+)/homework$', StudentHomeworkList.as_view(), name='detail_students'),
    url(r'^students/(?P<pk>\d+)/forms$', StudentFormList.as_view(), name='detail_students'),
    url(r'^students/(?P<pk>\d+)/attendance$', StudentAttendanceList.as_view(), name='detail_students'),
    url(r'^students/(?P<pk>\d+)/behavior$', StudentBehaviorList.as_view(), name='detail_students'),

    ###############   CLASS ENDPOINTS #################
    url(r'^classes/$', ListClasses.as_view(), name='list_classes'),
    url(r'^classes/(?P<pk>\d+)$', DetailClasses.as_view(), name='detail_classes'),
    url(r'^classes/(?P<pk>\d+)/events$', ClassEventList.as_view(), name='detail_classes'),
    url(r'^classes/(?P<pk>\d+)/fees$', ClassFeeList.as_view(), name='detail_classes'),
    url(r'^classes/(?P<pk>\d+)/students$', ClassStudentList.as_view(), name='detail_classes'),

    ###############   SCHOOL ENDPOINTS #################
    url(r'^schools/$', ListSchools.as_view(), name='list_schools'),
    url(r'^schools/(?P<pk>\d+)$', DetailSchools.as_view(), name='detail_schools'),
    url(r'^schools/(?P<pk>\d+)/classes$', SchoolClassList.as_view(), name='detail_schools'),
    url(r'^schools/(?P<pk>\d+)/events$', SchoolEventList.as_view(), name='detail_schools'),

    ###############   SCHOOL EVENT ENDPOINTS #################
    url(r'^school_events/$', ListSchoolEvents.as_view(), name='list_school_events'),
    url(r'^school_events/(?P<pk>\d+)$', DetailSchoolEvents.as_view(), name='detail_school_events'),

    ###############   CLASS EVENT ENDPOINTS #################
    url(r'^class_events/$', ListClassEvents.as_view(), name='list_class_events'),
    url(r'^class_events/(?P<pk>\d+)$', DetailClassEvents.as_view(), name='detail_class_events'),

    ###############   CLASS FEE ENDPOINTS #################
    url(r'^class_fees/$', ListClassFees.as_view(), name='list_class_fees'),
    url(r'^class_fees/(?P<pk>\d+)$', DetailClassFees.as_view(), name='detail_class_fees'),

    ###############   HOMEWORK ENDPOINTS #################
    url(r'^student_homework/(?P<pk>\d+)$', DetailStudentHomework.as_view(), name='detail_class_fees'),

    # ###############   FORM ENDPOINTS #################
    # url(r'^student_fees/(?P<pk>\d+)$', DetailStudentFees.as_view(), name='detail_class_fees'),
    #
    # ###############  ATTENDANCE ENDPOINTS #################
    # url(r'^student_attendance/(?P<pk>\d+)$', DetailStudentAttendance.as_view(), name='detail_class_fees'),
    #
    # ###############  BEHAVIOR ENDPOINTS #################
    # url(r'^student_behavior/(?P<pk>\d+)$', DetailStudentBehavior.as_view(), name='detail_class_fees'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
