# Generated by Django 4.1.4 on 2022-12-18 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0011_form_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='formrequest',
            name='ip',
            field=models.GenericIPAddressField(default=1),
            preserve_default=False,
        ),
    ]
