from django.db import models
from user.models import User # This imports the model from User to this article https://docs.djangoproject.com/en/1.10/topics/db/models/


# Create your models here.
class article(models.Model):
    authors = models.CommaSeparatedIntegerField(max_length=200)
    code = models.CharField(max_length=6)
    title = models.CharField(max_length=500)
    abstract = models.CharField(max_length=2000)
    scientific_question = models.CharField(max_length=500)
    main_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    create_date = models.DateTimeField('date created')
    views = models.IntegerField(default=0)


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)