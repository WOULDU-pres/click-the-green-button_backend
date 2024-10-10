from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.user_name

class GameResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='results')
    round = models.PositiveIntegerField()
    result = models.CharField(max_length=10)  # 반응 시간 (초 단위 문자열) 또는 '패배'
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user_name} - Round {self.round}: {self.result}"
