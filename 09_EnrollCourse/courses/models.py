from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=155,)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"

class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('COMPLETED', 'Completed'),
        ('DROPPED', 'Dropped'),
    ]
    student = models.ForeignKey('userApp.Student',on_delete=models.CASCADE,related_name='enrollments')
    course = models.ForeignKey('courses.Course',on_delete=models.CASCADE,related_name='enrollments')
    enrolled_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='ACTIVE')

    class Meta:
        unique_together = ('student', 'course')