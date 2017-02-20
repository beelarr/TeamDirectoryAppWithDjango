from django.db import models

# Create your models here.
class Person (models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.name