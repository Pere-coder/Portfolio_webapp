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
