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