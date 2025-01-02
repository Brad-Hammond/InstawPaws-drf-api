from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    """
    Post Model
    """
    tags_array = [
        ('Puppies', 'Puppies'),
        ('Training', 'Training'),
        ('Health', 'Health'),
        ('Grooming', 'Grooming'),
        ('Adoption', 'Adoption'),
        ('Nutrition', 'Nutrition'),
        ('Toys', 'Toys'),
        ('Walks', 'Walks'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    tags = models.CharField(max_length=30, choices=tags_array)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_tvgfiq', blank=True
    )