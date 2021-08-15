from django import urls
from django.views.generic.base import View
from .import views

from django.urls import path
urlpatterns=[
     path('course/', views.course_layout, name='course'),
     path('new/course/', views.course, name='new_course'),

 ]