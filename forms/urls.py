from django.contrib.auth.views import LoginView
from django.urls import path
from .views import *

app_name = 'base'

urlpatterns = [
    path('',home, name="home"),
    path("uz/", uz_redirect),
    path('signup/', create_account_view, name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("follow/<str:author>/",follow_toggle, name="follow"),
    path('new/', new_form_view, name='new'),
    path('create/<str:slug>/', create_dashboard_form_view, name="create_dashboard"),
    path("form/<str:slug>/", single_form_view, name='form'),
    path("dashboard/<str:slug>/", dashboard_from_view, name='dashboard'),
    path('submit-success/<str:slug>/', submit_success_view, name="submit_success"),
    path('request/<str:slug>/<int:pk>/', single_request_view, name='single_request'),
    path('notifications/', notifications_view, name='notifications'),
]