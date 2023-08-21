from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
class Author(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50, blank=True,default= 'Russia')
    def __str__(self):
        return self.name
class Genre(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    genres = models.ManyToManyField(Genre)
    publication_date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.title