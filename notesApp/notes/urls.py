from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('create/',views.create_note,name="create_note"),
    path('<int:note_id>/view',views.view_note,name="view"),
    path('<int:note_id>/edit',views.edit_note,name="edit_note"),
    path('<int:note_id>/delete',views.delete_note,name="delete_note"),
]


