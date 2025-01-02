from rest_framework import serializers
from likes.models import Like
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model.
    - Converts Post objects into JSON format for API responses.
    - Handles validation and ensures data integrity for posts.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    likes_total = serializers.ReadOnlyField()
    comments_total = serializers.ReadOnlyField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        """
        Validates the uploaded image for file size, height, and width.
        - Ensures the file size does not exceed 2MB.
        - Checks that the image height is no greater than 4096 pixels.
        - Verifies that the image width is no greater than 4096 pixels.
        - Raises a ValidationError if any of these conditions are violated.
        - Returns the image if all validations pass.
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value