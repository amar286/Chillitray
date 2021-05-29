
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    parent_id = models.CharField(max_length=10,null=True)

