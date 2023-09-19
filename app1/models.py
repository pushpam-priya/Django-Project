from email.policy import default
from django.db import models

# Create your models here.

class Dress(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateField(auto_now=True)
    type = models.CharField(max_length=100)
    gender = models.CharField(max_length=100,default='')
    pic = models.ImageField(upload_to='app1/images', default="")

    def __str__(self):
        return self.name

    



