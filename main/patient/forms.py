from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

class CustomAuthenticationForm(AuthenticationForm):
    # Override the error messages for invalid login and inactive account
    error_messages = {
        'invalid_login': "Invalid username or password.",
        'inactive': "This account is inactive.",
    }

    # The Meta class allows customization of widgets, labels, etc.
    class Meta:
        model = AuthenticationForm
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
        }
        labels = {
            'username': 'Username',
            'password': 'Password',
        }
        help_texts = {
            'username': 'Enter the username you used to register.',
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Manually applying custom widgets and placeholder values
        self.fields['old_password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your old password'
        })
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your new password'
        })
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Confirm your new password'
        })