from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import *
from forms.form import *

def home(request):
    return render(request, 'pages/home.html')

# Account Create
class CreateAccountView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateAccountForm

    def get_success_url(self):
        return reverse("base:login")

CreateAccountView = CreateAccountView.as_view()

# Profile View

def ProfileView(request, username):
    user_p = User.objects.get(username=username)
    user_forms = None
    user_requests = None
    if user_p.username == request.user.username:
        user_forms = user_p.form.all()
        user_requests = user_p.user_request.all()
    else:
        user_forms = user_p.form.filter(is_public=True)
        user_requests = user_p.user_request.filter(is_public=True)
    context = { 
        "user_p": user_p,    
        "user_forms":user_forms,
        "user_requests":user_requests
    }
    return render(request, 'pages/profile.html', context)


# @login_required(login_url='/')
def NewFormView(request):
    author = get_object_or_404(CustomUser, username=request.user)
    new_dash = None
    NewForm = CreateFormForm()
    if request.method == 'POST':
        NewForm = CreateFormForm(data=request.POST)
        if NewForm.is_valid():
            new_dash = NewForm.save(commit=False)     
            new_dash.slug = new_dash.created_on.strftime("%Y%m%d%H%M%S%f")
            new_dash.author = author
            new_dash.save()
            return redirect("base:single", new_dash.slug) 
   
    context={
        "NewForm":NewForm,
    }
    return render(request, "pages/new.html", context)

def SingleView(request, slug):
    single = Form.objects.get(slug=slug)
    form_q = get_object_or_404(Form, slug=slug)
    user_r = None
    if single.anonim_requests == False:
        if request.user.is_authenticated:
            user_r = get_object_or_404(CustomUser, username=request.user)
        else:
            return redirect('/')
    else:
        if request.user.is_authenticated:
            user_r = get_object_or_404(CustomUser, username=request.user)
        else:
            user_r = get_object_or_404(CustomUser, username='anonim')
    form_requests_count = form_q.request.count()
    new_request = None
    if request.method == 'POST':
        request_form = CreateFormRequestTest(data=request.POST)
        if request_form.is_valid():
            new_request = request_form.save(commit=False)
            new_request.form = form_q
            new_request.user = user_r
            new_request.save()
            return redirect("base:single", slug) # redirect to this url
    else:
        request_form = CreateFormRequestTest()
    context = {
        "single":single,
        "form_requests_count":form_requests_count,
        "request_form":request_form
    }
    return render(request, 'pages/single.html', context)