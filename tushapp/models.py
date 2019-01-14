from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
  
    image = models.ImageField(upload_to='product-images')
    name = models.CharField(max_length=30)
    price = models.IntegerField(max_length=30)
    category = models.CharField(max_length=30,null=True)


    @classmethod
    def display_product(cls,category):
        product = cls.objects.filter(category = category)
        return product

class Cart(models.Model):
    user = models.ForeignKey(User,related_name='cart')
    item = models.ForeignKey(Product,related_name='goodie')
    paid = models.CharField(default='False',max_length=20)

    def add_cart(self):
        return self.save()

    def delete_item(self):
        return self.delete()


    def __str__(self):
        return self.item.name

