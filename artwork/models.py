from django.db import models
from django.urls import reverse

# Create your models here.
class Artwork(models.Model):
        title = models.CharField(max_length=120)
        description = models.TextField(blank=True, null=True)
        price = models.DecimalField(decimal_places=2, max_digits=1000)
        width = models.TextField()
        height = models.TextField()
        artist = models.TextField(default='V.Galvao')
        available = models.BooleanField(null=True)
        images = models.ImageField(default='AG\images\default.PNG')

        def get_absolute_url(self):
                return reverse("artwork:artwork", kwargs={"id": self.id})  #f"/artwork/{self.id}/"

class SearchParams(models.Model):
        price = models.DecimalField(decimal_places=2, max_digits=1000)
        width = models.TextField()
        height = models.TextField()
        artist = models.TextField()
        user = models.TextField()


