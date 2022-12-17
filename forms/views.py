from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from forms.form import *

def home(request):
    return render(request, 'pages/home.html')

@login_required(login_url='app:login')
def NewFormView(request):
    author = get_object_or_404(CustomUser, username=request.user)
    # dash = author.form.all()
    new_dash = None
    NewForm = CreateFormForm()
    if request.method == 'POST':
        NewForm = CreateFormForm(data=request.POST)
        if NewForm.is_valid():
            new_dash = NewForm.save(commit=False)
            new_dash.title = new_dash.created_on
            new_dash.author = author
            new_dash.save()
            return redirect("/") 
   
    context={
        "NewForm":NewForm,
    }
    return render(request, "pages/new.html", context)

def RequestFormView(request, pk):

    pk = Form.objects.get(created_on=pk)
    context = {
        "pk":pk
    }
    return render(request, 'pages/formView.html', context)