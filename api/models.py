from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField()
    image = models.URLField()
    count = models.IntegerField()

    def __str__(self):
        return f"{self.title} -> {self.price}"
