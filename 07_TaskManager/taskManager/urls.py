from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('createproject',views.create_project,name='create_project'),
    path('createtask',views.create_task,name='create_task'),
]