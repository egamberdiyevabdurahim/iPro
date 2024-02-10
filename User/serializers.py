from rest_framework import serializers

from .models import User


class UserSer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=18, min_length=6, write_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'status', 'created_at')

    def create(self, validated_data):
        user = super().create(self.validated_data)
        user.set_password(validated_data.pop('password', None))
        user.save()
        return user
