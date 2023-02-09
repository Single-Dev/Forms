from .translater import TranslationOptions
from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Form)
admin.site.register(FormRequest)
admin.site.register(DashboardForm)