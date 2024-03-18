from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')
    
    def __str__(self):
        return f"{self.user.username} profile" 
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        
        if img.height > 300 and img.width >300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
    
