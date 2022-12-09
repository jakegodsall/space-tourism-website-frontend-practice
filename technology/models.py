from django.db import models
from django.urls import reverse

# Create your models here.


class Technology(models.Model):
    class Meta:
        verbose_name_plural = ("Technologies")

    name = models.CharField(max_length=128)
    description = models.TextField()
    portrait_image = models.ImageField()
    landscape_image = models.ImageField()
    slug = models.SlugField(default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("technology", args=[self.slug])
