from api.views import *
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^parent_students/$', ListParentStudent.as_view(), name='list_parents'),
    url(r'^parent_students/(?P<pk>\d+)$', DetailParents.as_view(), name='detail_parents'),
    url(r'^teachers/$', ListTeachers.as_view(), name='list_teachers'),
    url(r'^teachers/(?P<pk>\d+)$', DetailTeachers.as_view(), name='detail_teachers'),
    url(r'^students/$', ListStudents.as_view(), name='list_students'),
    url(r'^students/(?P<pk>\d+)$', DetailStudents.as_view(), name='detail_students'),
    url(r'^schools/$', ListSchools.as_view(), name='list_schools'),
    url(r'^schools/(?P<pk>\d+)$', DetailSchools.as_view(), name='detail_schools'),
    url(r'^classes/$', ListClasses.as_view(), name='list_classes'),
    url(r'^classes/(?P<pk>\d+)$', DetailClasses.as_view(), name='detail_classes'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
