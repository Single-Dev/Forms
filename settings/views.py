from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render

@login_required('base:login')
def password_change(request):
    form  = PasswordChangeForm(user=request.user, data=request.POST)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("base:profile", request.user.username)
    context={
        "form":form,
    }
    return render(request, "pages/settings/password_change.html", context )