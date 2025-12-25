from .models import Notes,Category
from django import forms

class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields= "__all__"

class CreateCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"