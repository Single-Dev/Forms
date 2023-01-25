# Generated by Django 4.1.4 on 2023-01-21 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0030_remove_profile_phone_remove_profile_telegram'),
    ]

    operations = [
        migrations.CreateModel(
            name='DashboardForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('views', models.IntegerField(default=1)),
                ('view_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('blocked_users', models.ManyToManyField(related_name='blocked', to=settings.AUTH_USER_MODEL)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dashboard_form', to='forms.form')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='view_form',
            field=models.ManyToManyField(blank=True, related_name='view_form', to='forms.dashboardform'),
        ),
    ]