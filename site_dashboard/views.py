from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .forms import *
User = get_user_model()

def home(request):
    template_name = 'admin/index.html'
    send_form = SendToEmailForm()
    if request.method == "POST":
        send_form = SendToEmailForm(request, data=request.POST)
        if send_form.is_valid():
            subject = send_form.cleaned_data.get("subject")
            message = send_form.cleaned_data.get("message")
            from_email = send_form.cleaned_data.get("email")
    
    recipient_list = User.objects.filter('email')
    send_mail(subject, message, from_email, recipient_list)
    context = {
        "send_form":send_form
    }
    return render(request, template_name)
