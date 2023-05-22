from django import forms
from forms.models import *

class FormPermissions(forms.ModelForm):
    class Meta:
        model = DashboardForm
        fields = ['blocked_users', 'users_cant_send','uwsr']