from django import forms
from .models import *

class SendToEmailForm(forms.ModelForm):
    class Meta:
        model = SubmitMsgToEmail
        fields= "__all__"