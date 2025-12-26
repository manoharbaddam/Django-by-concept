from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Journal(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    content = models.TextField()
    image = models.ImageField(upload_to='photos/',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} {self.user}"

