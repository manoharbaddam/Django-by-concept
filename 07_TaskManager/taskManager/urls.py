from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    
    path('createproject/',views.create_project,name='create_project'),
    path('viewprojects/',views.view_projects,name='view_projects'),
    path('<int:project_id>/editproject/',views.edit_project,name='edit_project'),
    path('<int:project_id>/deleteproject/',views.delete_project,name='delete_project'),

    path('createtask/',views.create_task,name='create_task'),
    path('<int:project_id>/viewtasks/',views.view_tasks,name='view_tasks'),
    path('<int:task_id>/edittasks/',views.edit_tasks,name ='edit_tasks'),
    path('<int:task_id>/deletetasks',views.delete_tasks,name='delete_tasks'),

    path('<int:project_id>/filteredtasks',views.filter_tasks,name='filter_tasks'),

]