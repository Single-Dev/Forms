from django.contrib.auth import get_user_model
from rest_framework import serializers
from forms.models import *

User = get_user_model()

# User API
class UsersApi(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username","email", "first_name", "last_name", "is_organiser", "is_agent",)