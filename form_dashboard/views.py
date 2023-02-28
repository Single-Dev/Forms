from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from forms.models import *
from forms.form import *

# ----------------------- Dashboard Form  ----------------------- #
# ----------------------- Dashboard

@login_required(login_url="base:login")
def dashboard_from_view(request, slug):
    user_requests = request.GET.get('user_requests')
    forma = Form.objects.get(slug=slug)
    requests = forma.form_requests.all()
    # ----- category request by username 
    if user_requests != None:
        if user_requests == "/anonim/":
            requests =forma.form_requests.filter(as_anonim=True)
        else:
            requests = forma.form_requests.filter(user__username=user_requests).filter(as_anonim=False)
    # ----- category request by username
    dashboard_obj = forma.dashboard_form
    if not forma.author == request.user:
        return redirect("base:form", slug)
    # ----------------------- Update Form view ----------------------- #
    update_forma = FormaForm(instance=forma)
    if request.method == 'POST':
        update_forma = FormaForm(request.POST, instance=forma)
        if update_forma.is_valid():
            update_forma.save()
            return redirect("fd:dashboard", slug)
    # ----------------------- Update Form view  End----------------------- #
    # ----------------------- Get Senders ----------------------- #
    sender_1 = forma.form_requests.all()
    senders =forma.form_requests.all()
    context = {
        "forma":forma,
        "dashboard_obj": dashboard_obj,
        "requests":requests,
        "senders":senders,
        "ufa": update_forma,
        # "page_obj":page_obj
    }
    return render(request, "fd/base.html", context)
# ----------------------- Dashboard
# ----------------------- Edit Form
@login_required(login_url='base:login')
def update_from(request, slug):
    forma = Form.objects.get(slug=slug)
    template_name = "fd/pages/edit-form.html"
    edit_forma = FormaForm(instance=forma)
    if request.method == 'POST':
        edit_forma = FormaForm(request.POST, instance=forma)
        if edit_forma.is_valid():
            edit_forma.save()
            return redirect("base:update_form", slug) 
    context = {
        "forma":forma,
        "edit_forma":edit_forma
    }
    return render(request, template_name, context)
# ----------------------- Form Edit end
# ----------------------- Form permissions
@login_required(login_url='base:login')
def form_permissions(request, slug):
    forma = Form.objects.get(slug=slug)
    template_name = "fd/pages/form-permissions.html"
    forma_permissions = FormPermissions(instance=forma.dashboard_form)
    if request.method == 'POST':
        forma_permissions = FormPermissions(request.POST, instance=forma.dashboard_form)
        if forma_permissions.is_valid():
            forma_permissions.save()
            return redirect("base:form_permissions", slug) 
    context = {
        "forma":forma,
        "forma_permissions":forma_permissions
    }
    return render(request, template_name, context)
# ----------------------- Form permissions End
# ----------------------- User Block toggle
@login_required(login_url='base:login')
def block_toggle(request, slug, user):
    forma = Form.objects.get(slug=slug)
    user = CustomUser.objects.get(username=user)
    blocked_users_list = forma.dashboard_form.blocked_users.all()

    if user in blocked_users_list:
        forma.dashboard_form.blocked_users.remove(user)
    elif not user in blocked_users_list:
        forma.dashboard_form.blocked_users.add(user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
# ----------------------- User Block toggle End
# ----------------------- Dashboard Form  End ----------------------- #