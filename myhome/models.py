from django.db import models

# Create your models here.

class HomePageInfo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='myhome/images')

    def __str__(self):
        return self.title
