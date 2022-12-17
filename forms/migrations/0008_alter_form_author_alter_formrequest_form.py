# Generated by Django 4.1.4 on 2022-12-17 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_alter_form_author_alter_formrequest_form_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='formrequest',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request', to='forms.form'),
        ),
    ]