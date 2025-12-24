
from .models import Notes
from django import forms

class CreateForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = "__all__"

