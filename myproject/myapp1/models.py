from django.db import models

# Create your models here.

class UserInfo(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    contact = models.PositiveIntegerField()
    email = models.EmailField()
    address = models.TextField()
    