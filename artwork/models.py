from django.db import models
from django.urls import reverse

# Create your models here.
class Artwork(models.Model):
        title = models.CharField(max_length=120)
        description = models.TextField(blank=True, null=True)
        price = models.DecimalField(decimal_places=2, max_digits=1000)
        width = models.IntegerField()
        height = models.IntegerField()
        artist = models.TextField(default='V.Galvao')
        available = models.BooleanField(null=True)
        images = models.ImageField(default='AG\images\default.PNG')
        year = models.IntegerField(default='0')

        def get_absolute_url(self):
                return reverse("artwork:artwork", kwargs={"id": self.id})  #f"/artwork/{self.id}/"

class SearchParam(models.Model):
        searchName = models.CharField(max_length=120, null=True)
        title = models.CharField(max_length=120, blank=True, null=True)
        price = models.DecimalField(decimal_places=2, max_digits=1000, blank=True, null=True)
        width = models.IntegerField(blank=True, null=True)
        height = models.IntegerField(blank=True, null=True)
        artist = models.CharField(max_length=120, blank=True, null=True)
        user = models.TextField(blank=True, null=True)
        year = models.IntegerField(blank=True, null=True)



