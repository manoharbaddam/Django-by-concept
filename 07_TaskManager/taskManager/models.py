from django.db import models
from customUser.models import CustomUserModel

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField(blank=True,null=True)
    owner = models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Task(models.Model):
    title = models.CharField(max_length=300)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"
