from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.core.exceptions import ValidationError

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**other_fields):
        if not email:
            raise ValueError("Enter Valid Email Address.")
        
        email = self.normalize_email(email)
        user = self.create(email=email,**other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)
        other_fields.setdefault("role", "ADMIN")


        if other_fields.get('is_superuser')==False:
            raise ValueError("Super User must have is_superuser set to True.")
        if other_fields.get('is_staff')==False:
            raise ValueError("Super User must have is_staff set to True.")
        
        return self.create_user(email,password,**other_fields)


class CustomUser(AbstractBaseUser,PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = "ADMIN","Admin"
        TEACHER = "TEACHER","Teacher"
        STUDENT = "STUDENT","Student"

    email = models.EmailField(unique=True,blank=False)
    username = models.CharField(max_length=125,unique=True)

    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)

    role = models.CharField(max_length=20,choices=Role.choices)

    # Teacher-specific
    registration_id = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)

    # Student-specific
    admission_no = models.CharField(max_length=50, blank=True, null=True, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username','role']


    def clean(self):
        if self.role == "TEACHER" and not self.registration_id :
            raise ValidationError("Teacher must have registration ID.")
        if self.role == "STUDENT" and not self.admission_no:
            raise ValidationError("Student must have Admission Number.")
    
    def __str__(self):
        return f"{self.email} ({self.role})"
    
