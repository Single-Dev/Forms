from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import *

User = get_user_model()

class CreateAccountForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    def clean_username(self):
        username = self.cleaned_data.get('username')  # get the username data
        lowercase_username = username.lower()         # get the lowercase version of it

        return lowercase_username

class CreateFormForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['title', 'is_public', 'anonim_requests', 'message']
    
class CreateFormRequestTest(forms.ModelForm):
    class Meta:
        model = FormRequest
        fields = ['is_public', 'full_name', 'email']