# Generated by Django 4.1.4 on 2023-03-04 16:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0047_alter_dashboardform_uwsr'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormVisits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visits', models.IntegerField(default=0)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
