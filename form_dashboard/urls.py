from django.urls import path
from .views import *

app_name = "fd"

urlpatterns = [
    path("requests-<str:slug>/", dashboard_from_view, name='dashboard'),
    path("edit-<str:slug>/", update_from, name='update_form'),
    path("permissions-<str:slug>/", form_permissions, name='form_permissions'),
    path("block/<str:slug>/<str:user>/", block_toggle, name='block_toggle'),
]