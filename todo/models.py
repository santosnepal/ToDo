from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True,auto_created=True)
    completed = models.BooleanField(default=False)