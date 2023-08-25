from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    profile_image = models.ImageField(upload_to='images/profile_images')
    email_active_code = models.CharField(max_length=80)
    about_user = models.TextField(null=True, blank=True)
