from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, AbstractUser
)

# Create your models here.

# class Register(models.Model):
#     username = models.CharField(max_length=255, unique=True, blank=False)
#     first_name = models.CharField(max_length=255, blank=False)
#     last_name = models.CharField(max_length=255, blank=False)
#     email = models.EmailField(max_length=255, blank=False, unique=True)
#     password = models.CharField(max_length=255, blank=False)
#     address = models.CharField(max_length=255, null=True)
#     city = models.CharField(max_length=255, blank=False)
#     state = models.CharField(max_length=255, blank=False)
#     zip_code = models.CharField(max_length=6,  blank=False)
#     country = models.CharField(max_length=255, blank=False)

#     def __str__(self):
#         return self.email


# class CustomUser(AbstractUser):
#     pass
#     # add additional fields in here

#     def __str__(self):
#         return self.username