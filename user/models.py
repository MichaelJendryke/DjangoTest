from django.db import models

# Create your models here.
class User(models.Model):
    fistname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100,blank=True)
    lastname = models.CharField(max_length=100)
    affiliation = models.CharField(max_length=100,blank=True)
    title = models.CharField(max_length=100,blank=True)
    create_date = models.DateTimeField('date created')
    lastactive_date = models.DateTimeField('last date active')
    birthday_date = models.DateTimeField('birthday')
