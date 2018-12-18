# チュートリアル2
> 機能を追加する課題で実装方法を確認

## 追加機能の概要
現在は、複数のユーザのツイートがごちゃ混ぜで表示されている。

- ごちゃまぜの図

home画面からユーザ名をクリックすると、そのユーザが投稿したツイートとユーザ情報を表示するプロフィールページを新たに作成する。

- 追加する機能のイメージ図


## 1.URLの割り当て
まずは，urls.pyを編集して，プロフィールページにURLを割り当てる．

ここで，今回追加する機能について整理する．
ユーザを指定し，そのユーザ専用のプロフィールページに表示するため，ユーザごとで表示するページが異なる．
urls.pyに各ユーザにURLを割り当てるのは，ユーザ数が動的に増えるため対応できない．
そこで，以下のように記述する．

**[ b3twitter/twitter_app/urls.py ]**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('home', views.home, name='home'),
    path('create_tweet', views.create_tweet, name='create_tweet'),
    path('profile/<string:user_name>', views.profile, name='profile') # 追加
]
```

このように記述することで，URLは，"profile/"の後にユーザ名(user_name)を表す値を指定することができる．
したがって，ブラウザでユーザ名が"tester"のユーザのプロフィールページを見る場合，以下のURLになる．
> http://localhost:8080/profile/tester

指定したユーザ名は，この後作成するviewsの関数の引数として受け取ることができる．
したがって，viewsの関数はユーザごとで違う振る舞いを行うことができる．



## 2.動作の追加
次に，ページにアクセスした際の動作をviews.pyに関数を追加して記述する


**[ b3twitter/twitter_app/views.py ]**
```Python
# 以下の関数を追加
def profile(request, user_name):
    target_user = User.objects.filter(username=user_name).first()
    if target_user:
        tweets = Tweet.objects.filter(user__username=target_user.username)
        queries = {'target_user': target_user, 'tweets': tweets}
        return render(request, 'twitter_app/profile.html', queries)

    return redirect(home)
```

今回の関数では上から，
1. 引数で受け取ったユーザ名を用いてユーザ情報を検索し，target_userに格納
2. 与えられたuserが存在することを確認 (存在しなければ，target_user = None)
3. ユーザがツイートした情報をusernameを用いてTweetモデルから検索し，tweetsに格納
4. ターゲットユーザとツイート情報をクエリーに格納
5. テンプレートと組み合わせて返す


## 3.テンプレート作成と再利用
テンプレートでは，homeのテンプレートで使われていた，受け取ったツイートを全て表示する機構がそのまま再利用できる．

以下の部分をtweets.htmlとして分割し．homeからは，上記の部分を削除する．

**[ b3twitter/twitter_app/templates/tweets.html ]**
```html
<div id="tweets">
    {% for tweet in tweets %}
    <div class="card">
      <div class="card-body">
        <div class="card-title" style="display: flex">
            <h5><u>{{ tweet.user.username }}</u></h5>
            <h6 class="text-muted" style="margin-left: auto">{{ tweet.created_at }}</h6>
        </div>

        <p class="card-text">{{ tweet.content }}</p>

        {% if request.user in tweet.likes.all %}
        <button id="like-btn"
                data-url="{% url "api_like_tweet" tweet.id %}"
                class="card-link btn btn-success">
            <span>Liked</span>
            <span class="badge badge-light">{{ tweet.likes.count }}</span>
        </button>
        {% else %}
        <button id="like-btn"
                data-url="{% url "api_like_tweet" tweet.id %}"
                class="card-link btn btn-outline-success">
            <span>Like</span>
            <span class="badge badge-light">{{ tweet.likes.count }}</span>
        </button>
        {% endif %}

      </div>
    </div>
    {% endfor %}
</div>

<script>
    $("#tweets").on("click", "#like-btn", function (event) {
        event.preventDefault();
        var this_ = $(this);

        this_.prop('disabled', true);
        $.ajax({
            url: this_.attr("data-url"),
            type: 'GET'
        }).done(function (data) {
            var like_count = Number(this_.children("span:last").text());
            if (data.is_liked){
                this_.removeClass().addClass("card-link btn btn-success");
                this_.children("span:first").text("Liked");
                this_.children("span:last").text(like_count+1);
            }else{
                this_.removeClass().addClass("card-link btn btn-outline-success");
                this_.children("span:first").text("Like");
                this_.children("span:last").text(like_count-1);
            }
            this_.prop('disabled', false);
        }).fail(function (data) {
            console.log('like api error');
            alert('Like処理に失敗しました．ログインしていますか？');
            this_.prop('disabled', false);
        });
    })
</script>
```

tweets.htmlを使用する場合は，以下のように記述する
```html
{%include 'tweets.html'%}
```

したがって，"home.html"は以下のようになる．

**[ b3twitter/twitter_app/templates/twitter_app/home.html ]**
```html
{% extends 'base.html' %}

{% block content %}
    <h1 class="mt-2">
        <div style="display: flex">
            <h3>login user : </h3>
            <h3 style="font-weight: bold;">{{ request.user }}</h3>
        </div>
    </h1>
    <hr class="mt-0 mb-4">

    {% load crispy_forms_tags %}
    <form action="{% url 'create_tweet' %}" method="post">
        {% csrf_token %}
        {{ tweet_form|crispy }}
        <button type="submit" class="btn btn-primary" id='tweet-btn'>tweet</button>
    </form>
    <hr class="mt-0 mb-4">

    <!-- 以下を追加 -->
    {%include 'tweets.html'%}
{% endblock %}
```

今回新たに作成するプロフィールページのテンプレートが"profile.html"として以下のようにする．

**[ b3twitter/twitter_app/templates/twitter_app/profile.html ]**
```html
{% extends 'base.html' %}

{% block content %}
    {% load crispy_forms_tags %}

    <h1 class="mt-2">
        <div style="display: flex">
            <h3 style="font-weight: bold;">{{ target_user.username }}</h3>
            <h3> のプロフィール </h3>
        </div>
    </h1>
    <hr class="mt-0 mb-4">

    {%include 'tweets.html'%}
{% endblock %}
```

> この状態で，以下のURLにアクセスすることで動作を確認できる．<br>
> http://localhost:8080/profile/[ユーザ名]


## 4.aタグを使ったリンク付け
最後にhtmlにaタグを使ってプロフィールページのリンクを追加する．

- aタグを貼る場所の図

3の工程で分割した"tweets.html"にツイートを表示する際に一緒に記載するユーザ名にリンクを貼る．
aタグは，Djangoで用意されてるURLの記述方法に従い以下のように記述する，
```html
<a href="{% url "profile" tweet.user.username %}"></a>
```

**b3twitter/twitter_app/templates/tweets.html**
```html
<div id="tweets">
    {% for tweet in tweets %}
    <div class="card">
      <div class="card-body">
        <div class="card-title" style="display: flex">
            <h5>
                <a href="{% url "profile" tweet.user.id %}">
                    <u>{{ tweet.user.username }}</u>
                </a>
            </h5>
            <h6 class="text-muted" style="margin-left: auto">{{ tweet.created_at }}</h6>
        </div>
<!-- 以下省略 -->
```
