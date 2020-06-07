from django.db import models


# Create your models here.

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=200, default="")
    date1 = models.DateField(null=True,default="")
    labels = models.CharField(max_length=50, default="Personal")
    status = models.CharField(max_length=50, default="New")
    priority = models.CharField(max_length=10, default="1")
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.task
