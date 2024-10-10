# game/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, GameResult
from .serializers import GameResultSerializer, UserSerializer
from django.shortcuts import get_object_or_404

# 게임 결과 저장 API

class GameResultView(APIView):
    def post(self, request):
        user_name = request.data.get('userName')
        round_number = request.data.get('round')
        result = request.data.get('result')

        if not user_name or not round_number or result is None:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

        # 사용자 가져오기 또는 생성
        user, created = User.objects.get_or_create(user_name=user_name)

        # 게임 결과 저장
        game_result = GameResult.objects.create(
            user=user,
            round=round_number,
            result=str(result)  # 숫자나 '패배'를 문자열로 저장
        )

        return Response({'message': 'Result saved successfully'}, status=status.HTTP_201_CREATED)

# 사용자별 결과 조회 API

class UserGameResultsView(APIView):
    def get(self, request):
        user_name = request.query_params.get('userName')

        if not user_name:
            return Response({'error': 'User name is required'}, status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(User, user_name=user_name)
        serializer = UserSerializer(user)

        return Response({'results': serializer.data['results']}, status=status.HTTP_200_OK)
