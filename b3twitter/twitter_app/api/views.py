from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import Tweet


class LikeAPIView(APIView):
    def get(self, request, tweet_id):
        tweet = Tweet.objects.filter(pk=tweet_id).first()
        if tweet:
            if request.user in tweet.likes.all():
                tweet.likes.remove(request.user)
            else:
                tweet.likes.add(request.user)
            return Response({'is_liked': request.user in tweet.likes.all()})

        return Response(None, status=400)
