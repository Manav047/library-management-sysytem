from django.db import models
from .models import *

# Create your models here.
class reader(models.Model):
    def __str__(self):
        return self.reader_name
    referece_id=models.CharField(max_length=200)
    reader_name=models.CharField(max_length=200)
    reader_contact = models.CharField(max_length=200)
    reader_address=models.TextField()
    active=models.BooleanField(default=True)



class Book(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)  # Default quantity is 0

    def __str__(self):
        return self.name
