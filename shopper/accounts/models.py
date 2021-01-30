from django.db import models
from django.db.models.constraints import CheckConstraint

# Create your models here.

class credentails(models.Model):
    cc      = models.CharField(max_length=50)
    email   = models.CharField(max_length=50)
    phone   = models.IntegerField()
    address = models.CharField(max_length=50)
    zip_code= models.CharField(max_length=50)

    def __str__(self):
        return self.email

    def __cc__(self):
        return self.cc

    def __phone__(self):
        return self.phone

    def __zip__(self):
        return self.zip_code

class links(models.Model):
    link = models.CharField(max_length=50)
    size  = models.IntegerField()

    def __str__(self):
        return self.link