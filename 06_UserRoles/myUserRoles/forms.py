from .models import CustomUser
from django import forms


class CustomUserForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["email", "first_name",'role']

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('password')!=cleaned.get('password2'):
            raise forms.ValidationError("Passwords doesn't match.")
        return cleaned
    
    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

        return user

class UserLoginForm(forms.Form):
    email = forms.EmailField(label="Email ")
    password = forms.CharField(label="Password ",widget=forms.PasswordInput)


