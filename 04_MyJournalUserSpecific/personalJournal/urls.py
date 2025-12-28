from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),  
    path('myjournal/',views.user_journal,name="user_journal"),
    path('create/',views.create_journal,name="create_journal"),
    path('<int:journal_id>/view/',views.view_journal,name='view_journal'),
    path('<int:journal_id>/edit/',views.edit_journal,name="edit_journal"),
    path('<int:journal_id>/delete/',views.delete_journal,name="delete_journal"),
    path('register/',views.register,name="register"),
    path('login/',views.login_view,name='login_view'),
    path('logout/',views.logout_view,name="logout_view"),
]   