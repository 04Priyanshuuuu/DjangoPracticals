from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title


class Movie(models.Model):
    name = models.CharField(max_length=200)
    rating = models.FloatField()
    review = models.TextField()

    def __str__(self):
        return self.name