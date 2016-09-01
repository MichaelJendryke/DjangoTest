from django.db import models

# Create your models here.
class article(models.Model):
    authors = models.CommaSeparatedIntegerField()
    code = models.CharField(max_length=6)
    title = models.CharField(max_length=500)
    abstract = models.CharField(max_length=2000)
    scientific_question = models.CharField(max_length=500)
    main_text = models.CharField()
    pub_date = models.DateTimeField('date published')
    create_date = models.DateTimeField('date created')
    views = models.IntegerField(default=0)


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)