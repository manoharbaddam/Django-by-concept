from django.urls import path
from userApp import views
from . import views

urlpatterns = [
    path('',views.view_courses,name="view_courses"),
    path('<int:course_id>/enroll/',views.enroll_course,name="enroll_course"),
    path('<int:course_id>/unenroll/',views.unenroll_course,name='unenroll_course'),
    path('dashboard/',views.dashboard,name='dashboard'),
]