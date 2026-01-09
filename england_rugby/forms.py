from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'message': 'Message',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].required = False


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(
                attrs={'Placeholder': 'Enter your password'}
            ),
            'password2': forms.PasswordInput(
                attrs={'Placeholder': 'Enter your password'}
            ),
            'name': forms.TextInput(
                attrs={'Placeholer': 'Enter your name'}
            ),
            'email': forms.TextInput(
                attrs={'Placeholder': 'Enter your email'}
            )
        }


class LoginForm(forms.Form):
    name = forms.CharField(max_length=20, label="Username")
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password'
        }), label="Password"
    )
