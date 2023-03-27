from django.urls import path
from .views import password_change
app_name ="settings"

urlpatterns=[
    path('password_change/', password_change, name='password_change'),
]