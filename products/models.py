from django.db import models
# Create your models here.
#from django.urls import reverse
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
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

class Comment(models.Model):
    PRODUCT_STARS=[
        ('1','very bad'),
        ('2','bad'),
        ('3','normal'),
        ('4','good'),
        ('5','perfect'),
                   ]
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments',)
    author=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='comments',)
    text=models.TextField(verbose_name='متن نظر شما')
    stars=models.CharField(max_length=10,choices=PRODUCT_STARS,verbose_name='امتیاز شما')
    datetime_created=models.DateTimeField(auto_now_add=True)
    datetime_modified=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)
    def get_absolute_url(self):
        return reverse('product_detail',args=[self.product.id])