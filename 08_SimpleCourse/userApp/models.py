from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from courses.models import Course

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**other_fields):
        if not email:
            raise ValueError("Enter valid email Id.")
        
        email = self.normalize_email(email)
        user = self.create(email = email,**other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**other_fields):
        other_fields.setdefault('is_active',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_staff',True)
        
        if other_fields.get('is_staff')==False:
            raise ValueError("Superuser should have is_staff set to True.")
        if other_fields.get('is_superuser')==False:
            raise ValueError("Superuser must have is_superuser set to True.")
        
        self.create_user(email=email,password=password,**other_fields)


class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=125,unique=True,)
    first_name  = models.CharField(max_length=125,blank=False,null=False)
    last_name = models.CharField(max_length=225,blank=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name',]

class Student(CustomUser):
    enrolled_courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.first_name}"