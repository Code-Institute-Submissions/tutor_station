from django.contrib import admin
from .models import Tutor, Subject

# Register your models here.


class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class TutorAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'name',
        'education',
        'description',
        'krona_per_hour',
        'image',
    )


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Tutor, TutorAdmin)