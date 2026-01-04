from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea
from .models import CustomUserModel


# Register your models here.
class UserAdminConfig(UserAdmin):
    model = CustomUserModel
    ordering = ("email","role")
    search_fields = ('email','user_name','first_name',)
    list_filter=('email','user_name','first_name','is_staff','is_active')
    list_display = ("email", "user_name", "role", "is_staff", "is_active")

    fieldsets = (
    ("Account", {
        "fields": (("email", "user_name"),)
    }),
    ("Personal Info", {
        "fields": (("first_name", "last_name"),)
    }),
    ("Role", {
        "fields": ("role",)
    }),
    ("Permissions", {
        "fields": ("is_staff", "is_active", "last_login")
    }),
)



    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "user_name",
                    "first_name",
                    "role",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


admin.site.register(CustomUserModel, UserAdminConfig)
