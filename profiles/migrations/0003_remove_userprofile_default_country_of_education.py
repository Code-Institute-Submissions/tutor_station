# Generated by Django 3.0.7 on 2020-06-29 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20200629_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_country_of_education',
        ),
    ]
