# Generated by Django 4.1.4 on 2023-01-21 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0035_rename_last_visit_dashboardform_view_on_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dashboardform',
            old_name='view_on',
            new_name='last_visit',
        ),
        migrations.RemoveField(
            model_name='dashboardform',
            name='views',
        ),
        migrations.AddField(
            model_name='dashboardform',
            name='visits',
            field=models.IntegerField(default=0),
        ),
    ]
