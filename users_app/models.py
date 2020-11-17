from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100, default="", blank=False)
    email = models.CharField(max_length=100, default="", blank=False)
    password = models.IntegerField(default=0)

    def __str__(self):
        return self.name
