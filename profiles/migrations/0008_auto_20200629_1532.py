# Generated by Django 3.0.7 on 2020-06-29 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20200629_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='description',
            new_name='default_description',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='education_level',
            new_name='default_education_level',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='price_per_hour',
            new_name='default_price_per_hour',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='subject_primary',
            new_name='default_subject_primary',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='subject_primary_other',
            new_name='default_subject_primary_other',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='subject_secondary',
            new_name='default_subject_secondary',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='subject_secondary_other',
            new_name='default_subject_secondary_other',
        ),
    ]