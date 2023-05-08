from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=500)
    content = models.CharField(max_length=5000)
    img = models.ImageField(upload_to='images/')
    

class IntroHeading(models.Model):
    value = models.CharField(max_length=500)

class IntroSubHeading(models.Model):
    value = models.CharField(max_length=500)

class About(models.Model):
    value = models.CharField(max_length=500)

class Email(models.Model):
    value = models.EmailField()

class Address(models.Model):
    value = models.CharField(max_length=500)