# Generated by Django 4.1.4 on 2023-01-21 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0034_alter_dashboardform_visits'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dashboardform',
            old_name='last_visit',
            new_name='view_on',
        ),
        migrations.RemoveField(
            model_name='dashboardform',
            name='visits',
        ),
        migrations.AddField(
            model_name='dashboardform',
            name='views',
            field=models.IntegerField(default=1),
        ),
    ]
