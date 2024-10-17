from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile

class RegisterForm(forms.Form):
    """User registration form."""
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'username'}
        )
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class':'form-control', 'placeholder':'password'}
        )
    )
    
    password2 = forms.CharField(
        label='confirmation password',
        widget=forms.PasswordInput(
            attrs={'class':'form-control', 'placeholder':'confirmation password'}
        )
    )
    
    def clean_username(self):
        """Ensure that the username is unique."""
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('User already exists.')
        
        return username
        
    def clean(self):
        """Validate that both passwords match."""
        cd = super().clean()
        p1, p2 = cd['password'], cd['password2']
        if p1 and p2 and p1 != p2:
            raise ValidationError('Passwords do not match.')
        
        

class LoginForm(forms.Form):
    """User login form."""
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'username'}
        )
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class':'form-control', 'placeholder':'password'}
        )
    )
    
    
    
class ProfileForm(forms.ModelForm):
    """User profile form."""
    
    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'first name'}
        )
    )
    
    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'last name'}
        )
    )
    
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={'class':'form-control', 'placeholder':'email'}
        )
    )
    
    
    class Meta:
        model = Profile
        exclude = ['user', 'score']
        
        widgets = {
            'age':forms.TextInput(attrs={'class':'form-control', 'placeholder':'age'}),
        }