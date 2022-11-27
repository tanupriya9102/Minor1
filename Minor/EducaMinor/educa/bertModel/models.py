from django.db import models

# Create your models here.
class Form(models.Model):
    ques=models.TextField()
    
class Contact(models.Model):
    name=models.CharField(max_length=50)
    mail=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    message=models.TextField()

