from django.db import models
from django.urls import reverse


class product(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=128)
    prix=models.FloatField(default=0.0)
    stock=models.IntegerField(default=0)
    desc=models.TextField(blank=True)
    thumbnail=models.ImageField(upload_to='product', blank=True, null=True)

    def __str__(self):
        return (f"{self.name}")

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug':self.slug})


