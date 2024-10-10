# game/serializers.py

from rest_framework import serializers
from .models import User, GameResult

class GameResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameResult
        fields = ['user', 'round', 'result', 'timestamp']

class UserSerializer(serializers.ModelSerializer):
    results = GameResultSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['user_name', 'results']
