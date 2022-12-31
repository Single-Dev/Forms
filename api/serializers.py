from rest_framework import serializers
from forms.models import *


# User API
class UsersApi(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        # fields = ("id", "username","email", "first_name", "last_name","date_joined","last_login","is_organiser", "is_agent", "user_permissions" )


# User API
class FormsApi(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'