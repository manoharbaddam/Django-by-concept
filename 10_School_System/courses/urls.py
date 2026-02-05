from django.urls import path
from . import views

app_name="courses"

urlpatterns = [
    path("create/", views.create_class, name="create_class"),
    path("classes/", views.class_list, name="class_list"),
    path('<str:username>/classes',views.student_enrollments,name="student_classes"),
]
