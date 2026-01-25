from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('',views.index,name="index"),
    path('dashboard/',views.dashboard_view,name="dashboard_view"),
    path('add_user/',views.add_user,name="add_user"),
    path('login_user/',views.login_user,name="login_user"),
    path('logout/',views.logout_user,name="logout_user"),
]   