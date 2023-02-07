from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth import logout
from django.contrib import messages
from django.utils import timezone
from .models import *
from forms.form import *

def home(request):
    n_count = None
    if request.user.is_authenticated:
        unread_notifys = FormRequest.objects.filter(view=False, form__author=request.user)
        n_count = unread_notifys.count()
    context={
        "n_count":n_count
    }
    return render(request, 'pages/main/home.html', context)

# Create User Account
def create_account_view(request):
    create_user_form = CreateAccountForm()
    login_form = AuthenticationForm()
    if request.method == 'POST':
        # ------------------------ User Login
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Siz {username} orqali ro'yhatdan o'tdingiz.")
                return redirect("base:profile", username)
            else:
                messages.error(request,"Foydalanuvchi nomi yoki parol xato")
                login_form = AuthenticationForm()
        # ------------------------ User Login
        # ------------------------ Signup
        create_user_form = CreateAccountForm(data=request.POST)
        if create_user_form.is_valid():
            create_user_form.save()
            return redirect("base:login")
        # ------------------------ Signup

    context={
        "cuf":create_user_form,
        "login_form":login_form
    }
    return render(request, 'registration/signup.html', context)

# Profile View
def profile_view(request, username):
    user_p = User.objects.get(username=username)
    if user_p.username == "anonim":
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # ----------------------- Profile Tab ----------------------- #
    user_forms = None
    user_requests = None
    title = f'@{user_p.username}'
    tab = request.GET.get('tab')
    if user_p.username == request.user.username:
        if tab == 'forms':
            user_forms = user_p.form.all()
            title = f"Your forms"
        elif tab =='requests':
            user_requests = user_p.user_request.all()
            title = f"Your requests"
    else:
        if tab == 'forms':
            user_forms = user_p.form.filter(is_public=True)
            title = f"@{user_p.username}'s - forms"
        elif tab == 'requests':
            user_requests = user_p.user_request.filter(is_public=True)
            title = f"@{user_p.username}'s - requests"
            # user_requests_count = user_requests.count()
    # ----------------------- Profile Tab End ----------------------- #
    # ----------------------- Update Profile ----------------------- #
    user_form = None
    profile_form = None
    if request.user.is_authenticated:
        if request.user == user_p:
            user_form = UpdateUserForm(instance=request.user)
            profile_form = UpdateProfileForm(instance=request.user.profile)
            if request.method == 'POST':
                user_form = UpdateUserForm(request.POST, instance=request.user)
                profile_form = UpdateProfileForm(request.POST,
                                                request.FILES,
                                                instance=request.user.profile)
                if user_form.is_valid() and profile_form.is_valid():
                    user_name = user_form.cleaned_data.get('username')
                    user_form.save()
                    profile_form.save()
                    return redirect("base:profile", user_name)
    # ----------------------- Update Profile ----------------------- #
    context = { 
        "user_p": user_p,    
        "user_forms":user_forms,
        "user_requests":user_requests,
        # "user_requests_count":user_requests_count,
        "title": title,
        "user_form":user_form,
        "profile_form":profile_form
    }
    return render(request, 'pages/main/profile.html', context)

def logout_view(request):
    logout(request)
    return redirect("base:home")

# Create Form View
@login_required(login_url='base:login')
def new_form_view(request):
    author = get_object_or_404(CustomUser, username=request.user)
    new_dash = None
    NewForm = FormaForm()
    if request.method == 'POST':
        NewForm = FormaForm(data=request.POST)
        if NewForm.is_valid():
            new_dash = NewForm.save(commit=False)     
            new_dash.slug = new_dash.created_on.strftime("%Y%m%d%H%M%S%f")
            new_dash.author = author
            new_dash.save()
            return redirect("base:create_dashboard", new_dash.slug) 
   
    context={
        "NewForm":NewForm,
    }
    return render(request, "pages/others/new.html", context)

# --------------------------------------------------------------------- #
def create_dashboard_form_view(request, slug):
    forma = Form.objects.get(slug=slug)
    DashboardForm.objects.create(form=forma)
    return redirect("base:dashboard", slug)
# --------------------------------------------------------------------- #

# ----------------------- Yagona Forma ko'rish manzili ----------------------- #
def single_form_view(request, slug):
    forma = Form.objects.get(slug=slug)
    dashboard_obj = forma.dashboard_form
    blocked_users = dashboard_obj.blocked_users.all()
    if not forma.author == request.user and not request.user in blocked_users:
        dashboard_obj.visits += 1
        dashboard_obj.last_visit = timezone.now()
        dashboard_obj.save()
    # Agar user bloklangan bo'lsa
    if request.user in blocked_users:
        return redirect("/")
    # ----------------------- shu formaga kelgan sorovlarni ko'rish ----------------------- #
    tab = request.GET.get('form')
    requests_ = None
    if tab == "requests":
        if request.user.username == forma.author.username:
            requests_ = forma.form_requests.all()
        else:
            requests_ = forma.form_requests.filter(is_public=True)
    # ----------------------- shu formaga kelgan sorovlarni ko'rish ----------------------- #
    # ----------------------- Sorov Yubirish uchun ----------------------- #
    form_ = get_object_or_404(Form, slug=slug)
    user_r = None
    # Agar Anonim Sorovlaar uchun ruxsat etilmagan bo'lsa
    if forma.anonim_requests == False:
        if request.user.is_authenticated:
            user_r = get_object_or_404(CustomUser, username=request.user)
        else:
            return redirect(f"/login/?next={request.path}")
    # Agar Anonim Sorovlaar uchun ruxsat etilmagan bo'lsa
    # Agar Anonim Sorovlaar uchun ruxsat etilgan bo'lsa
    else:
        if not request.user.is_authenticated:
            user_r = get_object_or_404(CustomUser, username='anonim')
        else:
            user_r = get_object_or_404(CustomUser, username=request.user)
    # Agar Anonim Sorovlaar uchun ruxsat etilgan bo'lsa
    form_requests_count = form_.form_requests.count()
    new_request = None
    request_form = None
    # Agar Foydalanuvchi formani yaratgan bo'lsa
    if forma.author == request.user:
        return redirect("base:dashboard", slug)
    else:
        if request.method == 'POST':
            request_form = CreateFormRequestTest(data=request.POST)
            if request_form.is_valid():
                new_request = request_form.save(commit=False)
                new_request.form = form_       
                new_request.user = user_r
                new_request.save()
                return redirect("base:submit_success", slug)
        else:
            request_form = CreateFormRequestTest()
    # ----------------------- Sorov Yubirish uchun ----------------------- #
    context = {
        "forma":forma,
        "form_requests_count":form_requests_count,
        "request_form":request_form,
        "requests_":requests_,
    }
    return render(request, 'pages/others/form.html', context)
# ----------------------- Yagona Forma ko'rish manzili ----------------------- #

# ----------------------- Dashboard Form  ----------------------- #
@login_required(login_url="base:login")
def dashboard_from_view(request, slug):
    user_requests = request.GET.get('user_requests')
    forma = Form.objects.get(slug=slug)
    requests = forma.form_requests.all()
    # ----- category request by username 
    if user_requests != None:
        if user_requests == "anonim":
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
            return redirect("base:dashboard", slug)
    # ----------------------- Update Form view  End----------------------- #
    # ----------------------- Get Senders ----------------------- #
    sender_1 = forma.form_requests.all()
    senders =None
    for su in sender_1:
        senders = forma.form_requests.filter(user__username=su.user.username)
    # for sender in requests:
    #     senders.append(sender)
    # ----------------------- Get Senders End ----------------------- #
    # ----------------------- Pagination  ----------------------- #
    page_number = request.GET.get('page')
    page_list = forma.form_requests.all()
    paginator  = Paginator(page_list, 2)
    requests = paginator.get_page(page_number)
    if page_number == None:
        requests = forma.form_requests.all()
    # ----------------------- Pagination End ----------------------- #
    context = {
        "forma":forma,
        "dashboard_obj": dashboard_obj,
        "requests":requests,
        "senders":senders,
        "ufa": update_forma,
        # "page_obj":page_obj
    }
    return render(request, "pages/others/dashboard.html", context)
# ----------------------- Dashboard Form  End ----------------------- #

# ----------------------- Request view ----------------------- #
@login_required(login_url='base:login')
def single_request_view(request, slug, pk):
    single_form = Form.objects.get(slug=slug)
    single_request = FormRequest.objects.get(id=pk)
    user_ = get_object_or_404(CustomUser, username=request.user)
    if single_request.is_public == True:
        pass
    else:
        if user_.username == single_form.author.username or user_.username == single_request.user.username:
            pass
        else:
            return redirect('base:home')
    if single_form.author.username == user_.username:
        single_request.view = True
        single_request.save()
    context = {
        'single_request':single_request,
        'single_form':single_form
    }
    return render(request, 'pages/others/request.html', context)
# ----------------------- request view End ----------------------- #

def submit_success_view(request, slug):
    single = Form.objects.get(slug=slug)
    context ={
        "single":single
    }
    return render(request, 'pages/helpers/success.html', context)

# ----------------------- Notifications view ----------------------- #
@login_required(login_url='base:login')
def notifications_view(request):
    unread_notifys = FormRequest.objects.filter(view=False, form__author=request.user)
    n_count = unread_notifys.count()
    context = {
        "unread_notifys":unread_notifys,
        "n_count":n_count
    }
    return render(request, 'pages/main/notifications.html', context)
# ----------------------- notifications view End----------------------- #

