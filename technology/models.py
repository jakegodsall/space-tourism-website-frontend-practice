from django.db import models
from django.urls import reverse

# Create your models here.


class Technology(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    portrait_image = models.CharField(max_length=128)
    landscape_image = models.CharField(max_length=128)
    slug = models.SlugField(default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("technology", args=[self.slug])
