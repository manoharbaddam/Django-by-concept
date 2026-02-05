from django.db import models
from users.models import CustomUser

# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=225)
    teacher = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,limit_choices_to={'role':'TEACHER'})
    department = models.CharField(max_length=100)
    start_date = models.DateField()

    is_active = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together  = ('name','department')


class Enrollment(models.Model):
    student= models.ForeignKey(CustomUser,on_delete=models.CASCADE,limit_choices_to={'role','STUDENT'})
    class_enrolled = models.ForeignKey(Class,on_delete=models.CASCADE,related_name='enrollments')
    enrolled_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together=('student','class_enrolled')

