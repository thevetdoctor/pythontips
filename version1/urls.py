#version1/urls.py

from django.conf.urls import url
from . import views
# from tipdaily.views import contact_list

app_name = 'version1'

urlpatterns = [
    # url('', contact_list, name='contact_list'),
    url('', views.contact_list, name='contact_list'),
]