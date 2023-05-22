from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models

class CustomUser(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    followers = models.ManyToManyField("self", blank=True, related_name="following", symmetrical=False)

class Profile(models.Model):
    class Meta:
        verbose_name = "My Profile"
        verbose_name_plural = "Profile"
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default="profile/profile_14TGeRN.png", upload_to="profile")
    bio = models.CharField(max_length=100, null=True, blank=True, default="")
    is_online = models.BooleanField(default=False)
    is_verify = models.BooleanField(default=False)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return f"id: {self.id}; user id: {self.custom_user.id}"

class Form(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='form')
    is_public = models.BooleanField(default=True)
    created_on = models.DateTimeField(("created on"), default=timezone.now)
    message = models.TextField(max_length=300, null=True, blank=True)
    anonim_requests = models.BooleanField(default=False)
    infinite_requests = models.BooleanField(default=False)
    def __str__(self):
        return f'id: {self.id}, Created on: {self.created_on.strftime("%T")}, author: {self.author}'
# class FormVisits(models.Model):
#     form = models.OneToOneField(Form, on_delete=models.CASCADE, related_name="visits")
#     visits = models.IntegerField(default=0)
#     date =  models.DateTimeField(default=timezone.now)
class DashboardForm(models.Model):
    form = models.OneToOneField(Form, on_delete=models.CASCADE, related_name="dashboard_form")
    visits = models.IntegerField(default=0)
    last_visit = models.DateTimeField(default=timezone.now)
    blocked_users = models.ManyToManyField(CustomUser, related_name="blocked")
    users_that_cannot_send_requests = models.ManyToManyField(CustomUser, related_name='users_that_cannot_send_requests')
    sent_the_request = models.ManyToManyField(CustomUser, related_name='sent_the_request')
    def __str__(self):
        return f"{self.form}, views={self.visits}"

class FormRequest(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name="form_requests")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='user_request')
    as_anonim = models.BooleanField(default=False)
    view = models.BooleanField(default=False)
    full_name = models.CharField(max_length=32)
    email = models.EmailField()
    description = models.TextField(max_length=70)
    submited_on = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'id: {self.id}'

