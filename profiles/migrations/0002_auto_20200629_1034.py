# Generated by Django 3.0.7 on 2020-06-29 10:34

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_country_of_education',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_education_level',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_name',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_price_per_hour',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_subject_primary',
            field=models.CharField(blank=True, choices=[('Swedish', 'Swedish'), ('English', 'English'), ('French', 'French'), ('German', 'German'), ('Maths', 'Maths'), ('SO', 'SO'), ('Science', 'Science'), ('Other', 'Other')], max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_subject_primary_other',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_subject_secondary',
            field=models.CharField(blank=True, choices=[('Swedish', 'Swedish'), ('English', 'English'), ('French', 'French'), ('German', 'German'), ('Maths', 'Maths'), ('SO', 'SO'), ('Science', 'Science'), ('Other', 'Other')], max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_subject_secondary_other',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_type',
            field=models.CharField(choices=[('Client', 'I am a Client'), ('Tutor', 'I am a Tutor')], default=1, max_length=80),
        ),
    ]
