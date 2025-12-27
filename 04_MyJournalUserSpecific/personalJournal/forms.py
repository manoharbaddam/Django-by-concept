from django import forms
from django.contrib.auth.forms import UserCreationForm,User
from .models import Journal

class JournalCreationForm(forms.ModelForm):
    class Meta(): 
        model = Journal
        fields = ['title','content','image']

class UserRegistrationForm(UserCreationForm):
    class Meta():
        model = User
        email = forms.EmailField()
        fields= ["username",'email','password1','password2']


