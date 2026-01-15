from django import forms
from .models import Course


class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class CourseEnrollForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
    

