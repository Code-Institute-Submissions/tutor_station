# Generated by Django 3.0.7 on 2020-06-28 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20200628_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_image_url',
        ),
    ]
