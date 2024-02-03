from django.db import models
from django.contrib.auth.models import AbstractUser

from accounts.managers import CustomUserManager
# Create your models here.


GENDER = [
    ('M', 'Male'),
    ('F', 'Female'),
]

ACCOUNT_TYPE = [
    ('1', 'Employee'),
    ('2', 'Employer')
]

class CustomUser(AbstractUser):
    username = None
    name = models.CharField(max_length=256)
    phone_num = models.BigIntegerField(null=True, blank= True)
    email = models.EmailField(unique=True, blank=False, error_messages={'unique':'A user with this mail already exists, Please try another email.'})

    account = models.CharField(choices=ACCOUNT_TYPE, max_length=1)
    gender = models.CharField(choices=GENDER, max_length=1)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name
    
    objects = CustomUserManager()