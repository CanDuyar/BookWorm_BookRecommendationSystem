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


class OneBook(object):
    def __init__(self, book_id=0, title='', writer='', genres='', page_num='',pub_year='',rating='',image_url='',isbn=''):
        self.book_id = book_id
        self.title = title
        self.writer = writer
        self.genres = genres
        self.page_num = page_num
        self.pub_year = pub_year
        self.rating = rating
        self.image_url = image_url
        self.isbn = isbn

    def as_dict(self):
        return {'book_id': self.book_id,'title': self.title, 'writer': self.writer,
                'genres': self.genres, 'page_num': self.page_num, 'pub_year': self.pub_year
                , 'rating': self.rating, 'image_url': self.image_url, 'isbn': self.isbn
                }
