# Generated by Django 4.1.4 on 2023-02-22 16:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0046_remove_customuser_following_customuser_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboardform',
            name='uwsr',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
