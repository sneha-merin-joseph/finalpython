
from django.db import models

#Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to='gallery')
    actors=models.TextField()
    release_date=models.DateField(null=True, blank=True)


class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name