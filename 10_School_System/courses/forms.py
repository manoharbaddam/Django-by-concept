from django import forms
from .models import Class
from users.models import CustomUser

class ClassCreateForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ("name", "department", "teacher","start_date")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # show only teachers
        self.fields["teacher"].queryset = CustomUser.objects.filter(
            role=CustomUser.Role.TEACHER
        )
