from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    title           = models.TextField(max_length=30)
    topic           = models.TextField(max_length=15)
    content         = models.TextField(default="Enter Content Here.")
    pub_date        = models.DateTimeField(auto_now_add=True)
    last_modified   = models.DateTimeField(auto_now=True)
    # allow_replies   = models.BooleanField(default=False) #TODO: No reason to have this with no way to save replies right now
    # replies         = #TODO: Currently not sure how to save array in model with sqlite3
    votes           = models.IntegerField(default=0)
