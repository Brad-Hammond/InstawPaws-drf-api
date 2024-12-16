from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    """
    Profile model class
    When User is created,
    Profile is created (OneToOneField)
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_wxgp9p'
    )
   