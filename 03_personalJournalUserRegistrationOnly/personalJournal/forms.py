from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

from .models import Journal

class JournalCreationForm(forms.ModelForm):
    class Meta():
        model = Journal
        fields= ['title','content','image']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



