from django.contrib.auth.views import LoginView
from django.urls import path
from .views import *

app_name = 'base'

urlpatterns = [
    path('', home, name="home"),
    path('new/', NewFormView, name='new'),
    path('signup/', CreateAccountView, name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path('logout/', logoutView, name='logout'),
    path('@<str:username>/', ProfileView, name="profile"),
    path("form/<str:slug>/", SingleView, name='single'),
    path('submit-success/<str:slug>/', SubmitSuccessView, name="submit_success"),
    path('notifications/', NotificationsView, name='notifications'),
    path('request/<str:slug>/<int:pk>/', SingleRequestView, name='single_request')
]
