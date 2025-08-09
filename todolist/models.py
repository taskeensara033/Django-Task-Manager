from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=70)
    desc=models.TextField()
    date=models.DateTimeField(auto_now=True)


class StudentHistory(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=70)
    desc=models.TextField()
    date=models.DateTimeField(auto_now=True)