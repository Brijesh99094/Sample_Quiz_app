from django.db import models

# Create your models here.
class Person(models.Model):

    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=50)

class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question