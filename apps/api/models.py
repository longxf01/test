from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()


class Task(models.Model):
    title = models.CharField(max_length=200)