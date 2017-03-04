from django.db import models

# Create your models here.
class Product(models.Model):
    category=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    description=models.CharField(max_length=1000)
    num_left=models.IntegerField()
    image=models.CharField(max_length=200)

    def __str__(self):
        return self.name