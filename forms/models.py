from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models

class CustomUser(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)

class Form(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='form')
    is_public = models.BooleanField(default=True)
    created_on = models.DateTimeField(("created on"), default=timezone.now)
    message = models.TextField(max_length=300)
    anonim_requests = models.BooleanField(default=False)

    def __str__(self):
        return f'id: {self.id} Created on: {self.created_on.strftime("%T")}'

class FormRequest(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE, )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='user_request')
    is_public = models.BooleanField(default=False)
    full_name = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return f'id: {self.id}'