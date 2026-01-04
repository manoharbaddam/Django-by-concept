from django import forms
from .models import Project,Task

class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields= ['name','description']

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
    
    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user')
        super().__init__(*args,**kwargs)

        self.fields["project"].queryset = Project.objects.filter(owner=user)