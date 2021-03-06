# Generated by Django 3.0.7 on 2020-06-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20200629_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='education_level',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='price_per_hour',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='subject_primary',
            field=models.CharField(blank=True, choices=[('Swedish', 'Swedish'), ('English', 'English'), ('French', 'French'), ('German', 'German'), ('Maths', 'Maths'), ('SO', 'SO'), ('Science', 'Science'), ('Other', 'Other')], max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='subject_primary_other',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='subject_secondary',
            field=models.CharField(blank=True, choices=[('Swedish', 'Swedish'), ('English', 'English'), ('French', 'French'), ('German', 'German'), ('Maths', 'Maths'), ('SO', 'SO'), ('Science', 'Science'), ('Other', 'Other')], max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='subject_secondary_other',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
