from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('home', views.home, name='home'),
    path('create_tweet', views.create_tweet, name='create_tweet'),
]
