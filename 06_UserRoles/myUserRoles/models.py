from django.db import models
from  django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**other_fields):
        if not email:
            raise ValueError("Enter Valid Email ID")

        email = self.normalize_email(email)
        user = self.model(email=email,**other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**other_fields):
        other_fields.setdefault('is_active',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_staff',True)

        if other_fields.get('is_staff')==False:
            raise ValueError("Super user must have is_staff set to True")
        if other_fields.get('is_superuser')==False:
            raise ValueError("Super user must have is_superuser set to True")
        
        return self.create_user(email,password,**other_fields)
        

class CustomUser(AbstractBaseUser,PermissionsMixin):

    roles = {
        'ADMIN':'Admin',
        'MEMBER':'Member',
        'GUEST' : 'Guest'
    }

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=225,blank=True)
    role = models.CharField(max_length=10,choices=roles)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','role']


    def __str__(self):
        return f"{self.first_name} {self.role}"


