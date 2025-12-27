from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Journal(models.Model):
    title = models.CharField(max_length=125)
    content = models.TextField()
    image = models.ImageField(upload_to='images/',blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
    
