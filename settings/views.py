from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render

@login_required(login_url='base:login')
def password_change(request):
    form  = PasswordChangeForm(user=request.user, data=request.POST)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("profile", request.user)
    context={
        "form":form,
    }
    return render(request, "settings/pages/password_change.html", context)