from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('create/',views.create_note,name="create_note"),
    path('<int:note_id>/view/',views.view_note,name="view_note"),
    path('<int:note_id>/edit/',views.edit_note,name="edit_note"),
    path('<int:note_id>/delete',views.delete_note,name="delete_note"),
    path('<int:cat_id>/categorynotes',views.category_notes,name='category_notes'),
    path('createcategory',views.create_category,name='create_category'),
]