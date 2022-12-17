from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from forms.form import *

def home(request):
    return render(request, 'pages/home.html')

@login_required(login_url='/')
def NewFormView(request):
    author = get_object_or_404(CustomUser, username=request.user)
    new_dash = None
    NewForm = CreateFormForm()
    if request.method == 'POST':
        NewForm = CreateFormForm(data=request.POST)
        if NewForm.is_valid():
            new_dash = NewForm.save(commit=False)
            new_dash.slug = new_dash.created_on.strftime("%f%S%M%H%d%m%Y")
            new_dash.author = author
            new_dash.save()
            return redirect("/") 
   
    context={
        "NewForm":NewForm,
    }
    return render(request, "pages/new.html", context)

def SingleView(request, slug):
    single = Form.objects.get(slug=slug)
    
    context = {
        "single":single
    }
    return render(request, 'pages/single.html', context)