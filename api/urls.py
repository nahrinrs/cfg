from django.conf.urls import patterns, include, url

# Function based API views
# from api.views import task_list, task_detail

# Class based API views
from api.views import ConfigList, ConfigDetail

urlpatterns = patterns('',

    # Regular URLs
    # url(r'^tasks/$', task_list, name='task_list'),
    # url(r'^tasks/(?P<pk>[0-9]+)$', task_detail, name='task_detail'),

    # Class based URLs,
    url(r'^configs/$', ConfigList.as_view(), name='config_list'),
    url(r'^configs/(?P<pk>[0-9]+)$', ConfigDetail.as_view(), name='config_detail'),
)
