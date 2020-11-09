from django.db import models


# Create your models here.
class BookClass(models.Model):
    name = models.CharField(max_length=100,default="", blank=False)
    genres = models.CharField(max_length=100,default="",blank=False)
    writer = models.CharField(max_length=100,default="", blank=False)
    isbn = models.IntegerField(default=0)
    publisher = models.CharField(max_length=100,default="", blank=False)
    rating = models.IntegerField(default=0)
    page_num = models.IntegerField(default=0)
    pub_year = models.IntegerField(default=0)

    def __str__(self):
        return self.name
