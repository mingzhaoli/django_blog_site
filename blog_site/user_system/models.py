from django.db import models

# Create your models here.
class User(models.Model):
    username        = models.TextField(max_length=15)
    password        = models.TextField(max_length=20) #TODO:TEMPORARY. FIGURE OUT HOW TO DO PASSWORD SAVING
    email           = models.EmailField()
    age             = models.IntegerField()
    # posts           = TODO: Currently not sure how to save array as a model with sqlite3
    # followers       = 
