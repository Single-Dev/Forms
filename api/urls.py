from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path("users/", UsersApiView, name='users'),
    path("user/<str:username>/", UserProfileApi, name="user_profile"),
    path("forms/", FormsApiView, name='forms'),
    path("form/<str:slug>/", OneFormApiView, name="one_form"),
    path("requests/", RequestsApiView, name="requests"),
]