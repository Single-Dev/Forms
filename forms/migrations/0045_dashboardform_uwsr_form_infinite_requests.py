# Generated by Django 4.1.4 on 2023-02-22 16:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0044_customuser_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardform',
            name='uwsr',
            field=models.ManyToManyField(related_name='submited', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='form',
            name='infinite_requests',
            field=models.BooleanField(default=False),
        ),
    ]