from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=225,blank=False,null=False)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.title}"
    
