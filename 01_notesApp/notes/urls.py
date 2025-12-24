from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('create/',views.create_note,name="create_note"),
    path('<int:note_id>/view_note',views.view_note,name="view_note"),
    path('<int:note_id>/edit_note',views.edit_note,name="edit_note"),
    path('<int:note_id>/delete_note',views.delete_note,name="delete_note"),
]


