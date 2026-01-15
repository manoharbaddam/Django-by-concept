from django.urls import path
from userApp import views
from . import views

urlpatterns = [
    path('',views.view_courses,name="view_courses"),
    path('enroll/',views.enroll_course,name="enroll_course"),
]