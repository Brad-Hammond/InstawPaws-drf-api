from rest_framework import serializers
from followers.models import Follower
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    '''
    A serializer for the Profile model to handle serialization and deserialization of profile data.
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    following_id = serializers.SerializerMethodField()
    posts_total = serializers.ReadOnlyField()
    followers_total = serializers.ReadOnlyField()
    following_total = serializers.ReadOnlyField()
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Determines if the currently authenticated user is the owner of the profile.
        - Compares the requesting user with the profile's owner.
        - Returns True if the user owns the profile; otherwise, False.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        '''
         Retrieves the ID of the "following" relationship if the authenticated user
         follows this profile's owner.
        - Checks if the user is authenticated.
        - Queries the Follower model to find a relationship where:
          - The requesting user is the owner.
          - The profile's owner is the followed user.
        - Returns the relationship ID if it exists; otherwise, None.
        '''
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:

        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'is_owner', 'following_id', 'posts_total',
            'followers_total', 'following_total'
        ]