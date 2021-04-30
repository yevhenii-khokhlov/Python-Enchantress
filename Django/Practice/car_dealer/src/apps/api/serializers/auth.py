from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class AuthAPISerializer(serializers.Serializer):
    username = serializers.CharField(max_length=25, required=False)
    password = serializers.CharField(max_length=30, required=False)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError('No such user')
        attrs['user'] = user
        return attrs

    def update(self, instance, validated_data):
        token = Token.objects.get(user=validated_data['user'])
        token.delete()
        token, created = Token.objects.get_or_create(user=validated_data['user'])
        return token

    def create(self, validated_data):
        token, created = Token.objects.get_or_create(user=validated_data['user'])
        return token
