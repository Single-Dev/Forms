# Generated by Django 4.1.4 on 2022-12-27 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0020_delete_submitsuccessmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='submit_success',
            field=models.TextField(default=1, max_length=700),
            preserve_default=False,
        ),
    ]