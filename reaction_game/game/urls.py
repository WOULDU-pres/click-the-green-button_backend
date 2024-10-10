# game/urls.py

from django.urls import path
from .views import GameResultView, UserGameResultsView

urlpatterns = [
    path('result/', GameResultView.as_view(), name='game_result'),
    path('results/', UserGameResultsView.as_view(), name='user_game_results'),
]
