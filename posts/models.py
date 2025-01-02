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

    class Meta:
        '''
        Defines metadata for the Post model.
        - Sets the default ordering of posts to newest first, based on the created_at field.
        '''
        ordering = ['-created_at']

    def __str__(self):
        '''
        Returns a string representation of the Post instance.
        - Combines the post ID and title for easier identification.
        '''
        return f'{self.id} {self.title}'