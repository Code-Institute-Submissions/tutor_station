from django.db import models


class Subject(models.Model):

    class Meta:
        verbose_name_plural = 'Subjects'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Tutor(models.Model):
    subject = models.ForeignKey('Subject', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    education = models.CharField(max_length=1024, null=True, blank=True)
    description = models.TextField()
    krona_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
