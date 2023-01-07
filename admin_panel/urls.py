
from django.urls import path
from .views import *

app_name = 'admin_panel'

urlpatterns = [
    path("", home, name="home")
]