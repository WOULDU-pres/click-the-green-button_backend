# reaction_game/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/game/', include('game.urls')),  # 추가된 부분
]
