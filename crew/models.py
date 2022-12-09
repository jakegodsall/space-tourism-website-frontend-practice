from django.db import models
from django.urls import reverse

# Create your models here.


class CrewMember(models.Model):

    class Meta:
        verbose_name_plural = 'Crew Members'

    name = models.CharField(max_length=128)
    role = models.CharField(max_length=64)
    bio = models.TextField()
    image = models.ImageField()
    slug = models.SlugField(default='')

    def __str__(self):
        return f"{self.role}: {self.name}"

    def get_absolute_url(self):
        return reverse("crew", args=[self.slug])
