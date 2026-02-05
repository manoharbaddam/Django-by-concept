from django.urls import path
from . import views

app_name="courses"

urlpatterns = [
    path("create/", views.create_class, name="create_class"),
    path("classes/", views.all_classes, name="all_classes"),
    path('<str:username>/classes',views.student_classes,name="student_classes"),
    path('enroll/<int:class_id>/', views.enroll_class, name='enroll_class'),
]
