from django.urls import path
from userApp import views

urlpatterns = [
    path('',views.index,name="index")
]