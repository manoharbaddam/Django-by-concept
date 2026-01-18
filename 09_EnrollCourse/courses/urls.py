from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('list_courses',views.list_courses,name="list_courses"),
    path('my_courses',views.my_courses,name="my_courses"),
    path('<int:course_id>/enroll_course',views.enroll_course,name="enroll_course"),
]
