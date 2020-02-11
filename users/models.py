from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'male'),
        ('F', 'female'),
        ('U', 'unknown'),
    ]
    birth_year = models.PositiveIntegerField(null=True, blank=True)
    about = models.CharField(max_length=200)
    join_date = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='U',
    )