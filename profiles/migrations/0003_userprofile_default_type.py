# Generated by Django 3.0.7 on 2020-06-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofile_default_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_type',
            field=models.CharField(choices=[('Tutor', 'I am a Tutor'), ('Client', 'I am a Client')], default=1, max_length=80),
        ),
    ]
