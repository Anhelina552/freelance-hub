from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Замовник'),
        ('freelancer', 'Фрілансер'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    profile_image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True)

# Create your models here.
