from django.db import models
from PIL import Image
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    product_name = models.CharField(max_length=40)
    description = models.TextField(max_length=200)
    minimum_order = models.IntegerField(default=True)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product_pics', default=None)
    
    
    def __str__(self):
        return self.product_name
    
    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'pk': self.pk})

    
    
    @property
    def discount(self):
        return self.price * 0.8
    
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        
        img = Image.open(self.image.path)
        
        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    

class CartItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} * {self.product}"
    

class Billing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Billing_User")
    fullname = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=10)
    telephone = models.CharField(max_length=15)

    def __str__(self):
        return self.fullname