from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Patient, Visit

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
        })
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control', 
        })
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control', 
        })

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'profile_picture']  # Add more fields as needed

    profile_picture = forms.ImageField(required=False)

class QuickPatientForm(forms.ModelForm):
    detail=forms.CharField(widget=forms.Textarea(attrs={'rows': '5'}))
    medicine_detail=forms.CharField(widget=forms.Textarea(attrs={'rows': '5'}))
    amount=forms.DecimalField(decimal_places=2, initial=0.0)
    next_visit=forms.IntegerField(initial=0)
    class Meta:
        model = Patient
        fields = ['name', 'email', 'age', 'gender']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'address': forms.Textarea(attrs={'rows': '5'}),
        }

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['detail', 'medicine_detail', 'amount', 'next_visit', 'note']
        widgets = {
            'detail': forms.Textarea(attrs={'rows': '5'}),
            'medicine_detail': forms.Textarea(attrs={'rows': '5'}),
            'note': forms.Textarea(attrs={'rows': '5'}),
        }