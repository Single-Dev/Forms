# Generated by Django 4.1.4 on 2023-03-18 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0049_delete_formvisits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formrequest',
            name='is_public',
        ),
    ]
