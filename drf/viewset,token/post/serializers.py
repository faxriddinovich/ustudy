from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField()
    email = serializers.EmailField(required=False)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    @property
    def _has_phone_field(self):
        return False

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', ''),
        }