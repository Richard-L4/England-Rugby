from django import forms
from .models import Contact, Register


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'address']
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'address': 'Postal Address',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].required = False
        self.fields['phone'].required = False


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name', 'email', 'password', 'address']
        widgets = {
            'password': forms.PasswordInput(
                attrs={'Placeholder': 'Enter your password'}
            ),
            'name': forms.TextInput(
                attrs={'Placeholer': 'Enter your name'}
            ),
            'email': forms.TextInput(
                attrs={'Placeholder': 'Enter your email'}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].required = False


class LoginForm(forms.Form):
    name = forms.CharField(max_length=20, label="Username")
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password'
        }), label="Password"
    )
