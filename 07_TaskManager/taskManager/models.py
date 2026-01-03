from django.db import models
from customUser.models import CustomUserModel

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=225)
    owner = models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    title = models.CharField(max_length=300)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    