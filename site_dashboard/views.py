from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .forms import *
User = get_user_model()

def home(request):
    template_name = 'dashboard/index.html'
    send_form = SendToEmailForm()
    subject = None
    message = None
    from_email = None
    if request.method == "POST":
        send_form = SendToEmailForm(request.POST)
        if send_form.is_valid():
            subject = send_form.cleaned_data.get("subject")
            message = send_form.cleaned_data.get("message")
            from_email = send_form.cleaned_data.get("email")
            send_form.save()
            return redirect('/dashboard')
    recipient_list = ["singledev68@gmail.com"]
    # send_mail(subject, message, from_email, recipient_list)
    context = {
        "send_form":send_form
    }
    return render(request, template_name, context)
