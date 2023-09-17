from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class PasswordCheckForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    def clean_password(self):
        password = self.cleaned_data.get('password')
        # check password strength
        if len(password) < 8:
            raise forms.ValidationError('Password is too short')
        return password

class RegistrationForm(UserCreationForm):
    # Add any additional fields you want to include in the registration form
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    # You can add custom fields or attributes to the login form if needed
    class Meta:
        model = User
