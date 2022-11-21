from django.db import models

# Create your models here.
class Forms(models.model):
    ques=models.TextField()
    date=models.DateField()
