from django.db import models


# Create your models here.
class BookClass(models.Model):
    title = models.CharField(max_length=100, default="", blank=False)
    writer = models.CharField(max_length=100, default="", blank=False)
    genres = models.CharField(max_length=100, default="", blank=False)
    page_num = models.IntegerField(default=0)
    pub_year = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    isbn = models.CharField(max_length=1000, default="", blank=False)
    image_url = models.TextField(default="", blank=False)

    def __str__(self):
        return self.title


class OneBook:
    title: str
    author: str
    genres: str
    page_num: int
    pub_year: int
    rating: int
    image_url: str
    isbn: int
