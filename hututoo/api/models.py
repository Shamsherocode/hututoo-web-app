
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from .manager import UserManager

class User(AbstractUser):
    username = None
    email = models.EmailField( unique=True)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    # def name(self):
    #     return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.email



class QuizCategory(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    img = models.ImageField(upload_to='media', blank=False, null=False)
    date = models.DateField()

    def __str__(self):
        return self.name


class QuizOption(models.Model):
    option1 = models.CharField(max_length=255, unique=False, blank=False)
    option2 = models.CharField(max_length=255, unique=False, blank=False)

    def __str__(self):
        return self.option1 + self.option2



class Quizs(models.Model):
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, null=False)
    created = models.DateTimeField()
    options = models.OneToOneField(QuizOption, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='media', blank=False, null=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    publish_date = models.DateTimeField()
    notice = models.TextField()

    def __str__(self):
        return self.name