# Generated by Django 4.1.4 on 2023-05-22 14:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0051_remove_customuser_view_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardform',
            name='users_cant_send',
            field=models.ManyToManyField(related_name='users_cant_send', to=settings.AUTH_USER_MODEL),
        ),
    ]
