from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('',views.index,name="index"),
    path('register/',views.register_user,name="register"),
    path('login_user/',views.login_user,name="login_user"),
    path('create_student/',views.create_student,name="create_student"),
    path('create_teacher/',views.create_teacher,name="create_teacher"),
]