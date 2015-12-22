from api.views import *
from django.conf.urls import url, include
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^api-token-auth/', ObtainAuthToken2.as_view()),

    url(r'^my_info/$', MyInfo.as_view(), name='my_info'),

    url(r'^parent_students/$', ParentStudentList.as_view(), name='list_parents'),
    url(r'^parent_students/(?P<pk>\d+)$', ParentStudentDetail.as_view(), name='detail_parents'),

    url(r'^parent_students_classes/$', ParentStudentClassList.as_view(), name='list_students_classes'),
    url(r'^parent_students_classes/(?P<pk>\d+)$', ParentStudentClassDetail.as_view(), name='detail_classes'),







    url(r'^parents/$', ParentList.as_view(), name='parent_list'),
    url(r'^parents/(?P<pk>\d+)$', ParentDetail.as_view(), name='parent_detail'),
    url(r'^parents/(?P<pk>\d+)/students$', ParentStudentsList.as_view(), name='parent_detail'),

    url(r'^students/$', ListStudents.as_view(), name='list_students'),
    url(r'^students/(?P<pk>\d+)$', DetailStudents.as_view(), name='detail_students'),
    url(r'^students/(?P<pk>\d+)/fees$', StudentFeeList.as_view(), name='detail_students'),
    url(r'^students/(?P<pk>\d+)/homework$', StudentHomeworkList.as_view(), name='detail_students'),
    url(r'^students/(?P<pk>\d+)/forms$', StudentFormList.as_view(), name='detail_students'),

    url(r'^teachers/$', ListTeachers.as_view(), name='list_teachers'),
    url(r'^teachers/(?P<pk>\d+)$', DetailTeachers.as_view(), name='detail_teachers'),
    url(r'^teachers/(?P<pk>\d+)/classes$', TeacherClassList.as_view(), name='detail_teachers'),

    url(r'^classes/$', ListClasses.as_view(), name='list_classes'),
    url(r'^classes/(?P<pk>\d+)$', DetailClasses.as_view(), name='detail_classes'),
    url(r'^classes/(?P<pk>\d+)/events$', ClassEventList.as_view(), name='detail_classes'),
    url(r'^classes/(?P<pk>\d+)/fees$', ClassFeeList.as_view(), name='detail_classes'),
    url(r'^classes/(?P<pk>\d+)/students$', ClassStudentList.as_view(), name='detail_classes'),


    url(r'^schools/$', ListSchools.as_view(), name='list_schools'),
    url(r'^schools/(?P<pk>\d+)$', DetailSchools.as_view(), name='detail_schools'),
    url(r'^schools/(?P<pk>\d+)/classes$', SchoolClassList.as_view(), name='detail_schools'),
    url(r'^schools/(?P<pk>\d+)/events$', SchoolEventList.as_view(), name='detail_schools'),




    url(r'^school_events/$', ListSchoolEvents.as_view(), name='list_school_events'),
    url(r'^school_events/(?P<pk>\d+)$', DetailSchoolEvents.as_view(), name='detail_school_events'),

    url(r'^class_events/$', ListClassEvents.as_view(), name='list_class_events'),
    url(r'^class_events/(?P<pk>\d+)$', DetailClassEvents.as_view(), name='detail_class_events'),

    url(r'^class_fees/$', ListClassFees.as_view(), name='list_class_fees'),
    url(r'^class_fees/(?P<pk>\d+)$', DetailClassFees.as_view(), name='detail_class_fees'),

    url(r'^class_fees/$', ListClassFees.as_view(), name='list_class_fees'),
    url(r'^student_homework/(?P<pk>\d+)$', DetailStudentHomework.as_view(), name='detail_class_fees'),


]

urlpatterns = format_suffix_patterns(urlpatterns)
