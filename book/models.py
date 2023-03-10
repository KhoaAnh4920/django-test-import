from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
