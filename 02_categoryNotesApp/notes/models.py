from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=225,unique=True,)


class Notes(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
