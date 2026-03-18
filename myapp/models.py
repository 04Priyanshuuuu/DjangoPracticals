from django.db import models
from datetime import date


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20)
    email = models.EmailField()
    branch = models.CharField(max_length=50)
    image = models.ImageField(upload_to='students/', blank=True, null=True)
    
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.FloatField()
    published_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
