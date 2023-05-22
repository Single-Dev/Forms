from django.urls import path
from .views import *

app_name = "fd"

urlpatterns = [
    path("requests-<str:slug>/", dashboard_form_view, name='dashboard'),
    path("edit-<str:slug>/", update_form, name='update_form'),
    path("permissions-<str:slug>/", form_permissions, name='form_permissions'),
    path("visits-<str:slug>/", form_visits_view, name='form_visits'),
    path("block/<str:slug>/<str:user>/", block_toggle, name='block_toggle'),
]