# Generated by Django 4.1.4 on 2023-01-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0036_rename_view_on_dashboardform_last_visit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='formrequest',
            name='description',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]