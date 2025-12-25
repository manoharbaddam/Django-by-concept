from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Journal

class JournalCreationForm(forms.ModelForm):
    class Meta():
        model = Journal
        fields= ['title','content','image']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        fields = ['username','email','password1','password2']



