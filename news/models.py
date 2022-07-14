from django.db import models

# Create your models here.

class News(models.Model):
    headline = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.headline