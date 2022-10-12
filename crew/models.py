from django.db import models
from django.urls import reverse

# Create your models here.


class CrewMember(models.Model):
    name = models.CharField(max_length=128)
    role = models.CharField(max_length=64)
    bio = models.TextField()
    image = models.CharField(max_length=128)
    slug = models.SlugField(default='')

    def __str__(self):
        return f"{self.role}: {self.name}"

    def get_absolute_url(self):
        return reverse("crew", args=[self.slug])
