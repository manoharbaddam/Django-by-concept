from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


# Create your models here.
class CustomUserManager(BaseUserManager):

    def create_user(self,email,password,**other_fields):
        if not email:
            raise ValueError("Enter the valid Email ID")
        
        email = self.normalize_email(email)
        user = self.model(
            email = email,**other_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError("Super user must have is_staff set to True")
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Super user must have is_superuser set to True ')

        return self.create_user(email,password,**other_fields)

class myCustomUserModel(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(verbose_name="Email ",unique=True)
    user_name = models.CharField(unique=True)
    first_name= models.CharField(max_length=150,)
    last_name = models.CharField(max_length=150,blank=True,null=True)
    
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['user_name','first_name']

    def __str__(self):
        return f"{self.email} {self.user_name}"
    