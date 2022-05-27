from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


# Create your models here.
class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email, password, **extra_fields)


# Create your models here.
class User(AbstractUser):
    username = None
    country = models.CharField(max_length=50, null=True, default=None)
    email = models.EmailField(unique=True)
    rented_books = models.IntegerField(default=0)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
  

    objects = CustomUserManager()

    def __str__(self):
        return self.email