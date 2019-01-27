from django import forms
from .models import BlogUser

class LoginForm(forms.ModelForm):
    class Meta:
        model = BlogUser
        fields = ('username', 'password',)

class RegisterForm(forms.ModelForm):
    class Meta:
        model = BlogUser
        fields = ('username', 'password','qq')
