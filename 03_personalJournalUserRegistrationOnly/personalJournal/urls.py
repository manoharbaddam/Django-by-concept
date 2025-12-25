from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('create/',views.create_journal,name="create"),
    path('<int:journal_id>view/',views.view_journal,name="view_journal"),
]