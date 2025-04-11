

# Create your models here.
from django.db import models

class BOOK(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.URLField(blank=True)

    def __str__(self):
        return self.title
