from django.urls import path
from .views import *

app_name = 'base'

urlpatterns = [
    path('', home, name="home"),
    path('new/', NewFormView, name='new'),
    path("form/<str:slug>/", SingleView, name='single'),
    path('signup/', CreateAccountView, name="signup")
]
