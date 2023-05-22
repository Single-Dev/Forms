from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils import timezone
from .models import *
from forms.form import *
from django.views.generic import TemplateView

# ---- Home ---- #
def home(request):
    n_count = None
    if request.user.is_authenticated:
        unread_notifys = FormRequest.objects.filter(view=False, form__author=request.user)
        n_count = unread_notifys.count()
    context={
        "n_count":n_count
    }
    return render(request, 'base/pages/main/home.html', context)
# ---- Home End ---- #
# ---- /uz/ resirect ---- #
def uz_redirect(request):
    return redirect('base:home')
# ---- /uz/ resirect end ---- #


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
                return redirect("profile", username)
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
    # ----------------------- Profile Tab ----------------------- #
    user_followers = None
    user_following = None
    user_forms = None
    user_requests = None
    title = f'@{user_p.username}'
    tab = request.GET.get('tab')
    if user_p.username == request.user.username:
        if tab == "followers":
            user_followers = user_p.followers.all()
            title = "Your followers"
        elif tab == "following":
            user_following = user_p.following.all()
            title = "You are a follower"
        elif tab == 'forms':
            user_forms = user_p.form.all()
            title = f"Your forms"
        elif tab =='requests':
            user_requests = user_p.user_request.all()
            title = f"Your requests"
    else:
        if tab == "followers":
            user_followers = user_p.followers.all()
            title = f"@{user_p.username}`s - followers"
        elif tab == "following":
            user_following = user_p.following.all()
            title = f"@{user_p.username}`s - following"
        elif tab == 'forms':
            user_forms = user_p.form.filter(is_public=True)
            title = f"@{user_p.username}`s - forms"
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
                    return redirect("profile", user_name)
    # ----------------------- Update Profile ----------------------- #
    context = { 
        "user_p": user_p,
        "user_followers":user_followers,
        "user_following":user_following,
        "user_forms":user_forms,
        "user_requests":user_requests,
        # "user_requests_count":user_requests_count,
        "title": title,
        "user_form":user_form,
        "profile_form":profile_form
    }
    return render(request, 'base/pages/main/profile.html', context)

def follow_toggle(request, author):
    if request.user.is_authenticated:
        authorObj = User.objects.get(username=author)
        request_user = User.objects.get(username=request.user.username)
        followers = authorObj.followers.all()

        if author != request_user.username:
            if request_user in followers:
                authorObj.followers.remove(request_user.id)
            else:
                authorObj.followers.add(request_user.id)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('base:login')

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
    return render(request, "base/pages/main/new.html", context)

# --------------------------------------------------------------------- #
def create_dashboard_form_view(request, slug):
    forma = Form.objects.get(slug=slug)
    DashboardForm.objects.create(form=forma)
    return redirect("fd:dashboard", slug)
# --------------------------------------------------------------------- #

# ----------------------- Yagona Forma ko'rish manzili ----------------------- #
def single_form_view(request, slug):
    forma = Form.objects.get(slug=slug)
    dashboard_obj = forma.dashboard_form
    blocked_users = dashboard_obj.blocked_users.all()
    list_of_sent_the_request = dashboard_obj.sent_the_request.all()
    if not forma.author == request.user and not request.user in blocked_users and not request.user in list_of_sent_the_request:
        dashboard_obj.visits += 1
        dashboard_obj.last_visit = timezone.now()
        dashboard_obj.save()
    # Agar user bloklangan bo'lsa
    if request.user in blocked_users:
        return render(request, 'base/pages/helpers/404.html')
    
    # Foydalanuvchilar bir marta sororv yuborish uchun
    users_who_sent_requests = forma.form_requests.all()
    if not forma.infinite_requests and request.user != forma.author:
        for user_who_sent_requests in users_who_sent_requests:
            dashboard_obj.users_that_cannot_send_requests.add(user_who_sent_requests.user.id)
    
    if request.user != forma.author:
        for user_who_sent_requests in users_who_sent_requests:
            dashboard_obj.sent_the_request.add(user_who_sent_requests.user.id)

    if request.user in dashboard_obj.users_that_cannot_send_requests.all():
        return redirect("base:submit_success", slug)
    # Foydalanuvchilar bir marta sororv yuborish uchun


    # ----------------------- shu formaga kelgan sorovlarni ko'rish ----------------------- #
    tab = request.GET.get('form')
    requests_ = None
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
        return redirect("fd:dashboard", slug)
    else:
        if request.method == 'POST':
            request_form = CreateFormRequestTest(data=request.POST)
            if request_form.is_valid():
                new_request = request_form.save(commit=False)
                new_request.form = form_       
                new_request.user = user_r
                if user_r.username == "anonim":
                    new_request.as_anonim = True
                new_request.save()
                return redirect("base:submit_success", slug)
        else:
            request_form = CreateFormRequestTest()
    # ----------------------- Sorov Yubirish uchun ----------------------- #
    context = {
        "forma":forma,
        "form_requests_count":form_requests_count,
        "request_form":request_form,
    }
    return render(request, 'base/pages/main/form.html', context)
# ----------------------- Yagona Forma ko'rish manzili ----------------------- #

# ----------------------- Request view ----------------------- #
@login_required(login_url='base:login')
def single_request_view(request, slug, pk):
    single_form = Form.objects.get(slug=slug)
    single_request = FormRequest.objects.get(id=pk)
    user_ = get_object_or_404(CustomUser, username=request.user)
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
    return render(request, 'base/pages/main/request.html', context)
# ----------------------- request view End ----------------------- #
@login_required(login_url='base:login')
def submit_success_view(request, slug):
    request_id = None
    forma = Form.objects.get(slug=slug)
    for requests in forma.form_requests.all():
        if requests.user.username == request.user.username:
                request_id = requests.id
    this_forms_requests = None
    if request.GET.get('view') == 'all':
        this_forms_requests = request.user.user_request.filter(form=forma)
    context ={
        "forma":forma,
        'request_id': request_id,
        'this_forms_requests': this_forms_requests
    }
    return render(request, 'base/pages/helpers/success.html', context)

# ----------------------- Notifications view ----------------------- #
@login_required(login_url='base:login')
def notifications_view(request):
    unread_notifys = FormRequest.objects.filter(view=False, form__author=request.user)
    n_count = unread_notifys.count()
    context = {
        "unread_notifys":unread_notifys,
        "n_count":n_count
    }
    return render(request, 'base/pages/main/notifications.html', context)
# ----------------------- notifications view End----------------------- #



def handler404(request, exception):
    return render(request, "base/pages/helpers/404.html")

def handler500(request, *args, **argv):
    return render(request, 'base/hpages/elpers/404.html')
