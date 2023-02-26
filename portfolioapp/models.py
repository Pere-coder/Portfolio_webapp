from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class photos(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')
    
    


class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    # def __str__(self):
    #     return f"{self.name}  {self.email}   {self.message}"
