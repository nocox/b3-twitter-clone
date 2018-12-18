from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')

    def __str__(self):
        return self.content
