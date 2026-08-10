from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50,unique = True)
    color = models.CharField(max_length = 50,blank=True)
    def __str__(self):
        return self.name

class Task(models.Model):
    PRIORITY_CHOICES = [
    ("L", "Low"),
    ("M", "Medium"),
    ("H", "High"),
]
    title = models.CharField(max_length = 100)
    description = models.TextField(blank = True)
    Completed = models.BooleanField(default = False)
    priority = models.CharField(max_length=200,choices=PRIORITY_CHOICES,default='M')
    due_date = models.DateField(null = True,blank =True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.title