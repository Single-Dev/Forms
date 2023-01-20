from django.core.files.images import get_image_dimensions
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

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', "username", "email"]

    def clean_username(self):
        username = self.cleaned_data.get('username')  # get the username data
        lowercase_username = username.lower()         # get the lowercase version of it

        return lowercase_username

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', "bio", "instagram", "github", "link", "address", "twitter"]
    
    def clean_avatar(self):
        avatar = self.cleaned_data['image']

        try:
            w, h = get_image_dimensions(avatar)

            #validate dimensions
            max_width = max_height = 100
            if w == max_width or h == max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                     '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')

            #validate file size
            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')

        except AttributeError:

            pass

        return avatar

class FormaForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['title', 'is_public', 'anonim_requests', 'message']
    
class CreateFormRequestTest(forms.ModelForm):
    class Meta:
        model = FormRequest
        fields = ['is_public', 'full_name', 'email', 'as_anonim']