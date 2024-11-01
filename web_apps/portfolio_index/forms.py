from django import forms
from .models import Contact
from django.contrib.auth.forms import AuthenticationForm

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']



class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'})
    )
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})
    )

    def confirm_login_allowed(self, user):
        # Optionally add custom logic to confirm the user's login
        if not user.is_active:
            raise forms.ValidationError("This account is inactive.", code='inactive')
