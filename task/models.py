from django.db import models
from category.models import Category
# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=30)
    category = models.ManyToManyField(Category)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    assignDate = models.DateField()
    def __str__(self):
        return self.taskTitle