from django.db import models
from django.urls import reverse

# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    distance = models.CharField(max_length=128)
    travel = models.CharField(max_length=128)
    image = models.ImageField()
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('destination', args=[self.slug])
