from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_pages = models.IntegerField(default=0)
    genre=models.CharField(max_length=100, default='Other')
    language = models.CharField(max_length=100, blank=True)
    edition=models.CharField(max_length=200, blank=True)
    cover = models.ImageField(upload_to='covers/', default='covers/default.jpg')

    def __str__(self):
        return self.title