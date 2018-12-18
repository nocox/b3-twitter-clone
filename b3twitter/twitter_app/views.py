from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import Tweet
from .forms import TweetForm


def top(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'twitter_app/top.html')


@login_required
def home(request):
    tweets = Tweet.objects.all().order_by("created_at").reverse()
    tweet_form = TweetForm(None)
    queries = {'tweets': tweets, 'tweet_form': tweet_form}
    return render(request, 'twitter_app/home.html', queries)


@login_required
def create_tweet(request):
    new_tweet = TweetForm(request.POST or None)
    if new_tweet.is_valid():
        tweet = Tweet(user=request.user, content=new_tweet.instance.content)
        tweet.save()
    return redirect(home)
