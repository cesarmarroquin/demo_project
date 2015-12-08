from api.views import *
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^parents/$', ListParents.as_view(), name='list_parents'),
    url(r'^parents/(?P<pk>\d+)$', DetailParents.as_view(), name='detail_parents'),
    url(r'^teachers/$', ListTeachers.as_view(), name='list_teachers'),
    url(r'^teachers/(?P<pk>\d+)$', DetailTeachers.as_view(), name='detail_teachers'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
