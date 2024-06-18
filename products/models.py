from django.db import models
# Create your models here.
#from django.urls import reverse
from django.shortcuts import reverse
class Product(models.Model):
    title=models.CharField(max_length=120)
    description=models.TextField()
    price=models.PositiveIntegerField(default=0)
    status=models.BooleanField(default=True)
    datetime_created=models.DateTimeField(auto_now_add=True)
    datetime_modified=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('product_detail',args=[self.pk])
