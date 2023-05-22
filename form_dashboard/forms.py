from django import forms
from forms.models import *

class FormPermissions(forms.ModelForm):
    class Meta:
        model = DashboardForm
        fields = ['blocked_users', 'users_that_cannot_send_requests','sent_the_request']