from django import forms
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"placeholder": "Enter password"})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm password"})
    )

    class Meta:
        model = CustomUser
        fields = ("email", "username","role")

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        validate_password(password)  # Django password validators
        return password

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.role = CustomUser.Role.STUDENT  # 🔒 force student role

        if commit:
            user.save()
        return user

class StudentCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ("email", "username", "admission_no")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = CustomUser.Role.STUDENT
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    
class TeacherCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ("email", "username", "registration_id", "department")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = CustomUser.Role.TEACHER
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user



class LoginForm(forms.Form):
    email = forms.EmailField(label="Email ID")
    password = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"placeholder":"Enter Password"}))
