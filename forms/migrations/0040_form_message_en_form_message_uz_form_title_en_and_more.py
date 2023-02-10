# Generated by Django 4.1.4 on 2023-02-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0039_formrequest_submited_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='message_en',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='form',
            name='message_uz',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='form',
            name='title_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='form',
            name='title_uz',
            field=models.CharField(max_length=50, null=True),
        ),
    ]