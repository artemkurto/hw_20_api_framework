from rest_framework import serializers
from .models import User
from .models import JobPosition
from .models import UserJobPosition


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = ['id', 'name']


class UserJobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserJobPosition
        fields = ['user', 'job_position']

    def create(self, validated_data):
        return UserJobPosition.objects.create(**validated_data)