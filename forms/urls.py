from django.contrib.auth.views import LoginView
from django.urls import path
from .views import *

app_name = 'base'

urlpatterns = [
    path('', home, name="home"),
    path('signup/', CreateAccountView, name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path('logout/', logoutView, name='logout'),
    path('@<str:username>/', ProfileView, name="profile"),
    path('new/', NewFormView, name='new'),
    path('create/<str:slug>/', CreateDashBoardFormView, name="create_dashboard"),
    path("form/<str:slug>/", SingleFormView, name='form'),
    path("dashboard/<str:slug>/", DashboardFromView, name='dashboard'),
    path('update/<str:slug>/', UpdateFormView, name="update_forma"),
    path('submit-success/<str:slug>/', SubmitSuccessView, name="submit_success"),
    path('request/<str:slug>/<int:pk>/', SingleRequestView, name='single_request'),
    path('notifications/', NotificationsView, name='notifications'),
]
