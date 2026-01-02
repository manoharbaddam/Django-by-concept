from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


# refer 3.10. User authentication in Django
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_staff", True)

        if other_fields.get("is_staff") == False:
            raise ValueError("SuperUser should have is_staff field set to True.")
        if other_fields.get("is_superuser") == False:
            raise ValueError("SuperUser should have is_superuser field set to True.")

        self.create_user(email=email, password=password, **other_fields)


class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=125)
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=225, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name", "first_name"]

    def __str__(self):
        return f"{self.user_name} {self.email}"
