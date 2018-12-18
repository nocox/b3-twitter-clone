from django.urls import path
from .views import LikeAPIView

urlpatterns = [
    path('like_tweet/<int:tweet_id>', LikeAPIView.as_view(), name='api_like_tweet')
]