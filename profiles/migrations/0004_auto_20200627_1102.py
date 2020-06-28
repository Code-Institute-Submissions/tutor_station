# Generated by Django 3.0.7 on 2020-06-27 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_userprofile_default_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_type',
            field=models.CharField(choices=[('Tutor', 'I am a Tutor'), ('Client', 'I am a Client')], default=2, max_length=80),
        ),
    ]
