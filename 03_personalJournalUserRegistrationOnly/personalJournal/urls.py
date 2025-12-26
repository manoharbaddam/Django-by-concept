from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('login/', views.login_view, name='login'),
    path('create/',views.create_journal,name="create"),
    path('<int:journal_id>/edit/',views.edit_journal,name="edit_journal"),
    path('<int:journal_id>view/',views.view_journal,name="view_journal"),
    path('logout/',views.logout_view,name="logout_view"),
]