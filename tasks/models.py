from django.db import models

# Create your models here.
class Task(models.Model):
    description=models.CharField(max_length=75)
    created_at=models.DateTimeField(auto_now=True)