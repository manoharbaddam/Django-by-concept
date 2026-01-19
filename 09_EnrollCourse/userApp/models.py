from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**other_fields):
        if not email:
            raise ValueError("Enter valid Email Id.")
        
        email = self.normalize_email(email)

        user = self.create(email=email,**other_fields)
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self,email,password,**other_fields):
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_superuser')==False:
            raise ValueError("Superuser should have is_staff set to True.")
        if other_fields.get('is_staff')==False:
            raise ValueError("Superuser should have is_staff set to True.")
        
        self.create_user(email=email,password=password,**other_fields)

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField()
    last_name = models.CharField()
    enrolled_courses = models.ManyToManyField('courses.Course')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default = False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name']
