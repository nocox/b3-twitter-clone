from django import forms
from .models import Tweet


class TweetForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                           'rows': '5',
                                                           'placeholder': 'What\'s happening?',
                                                           'id': 'tweet-content'}),
                              label='')

    class Meta:
        model = Tweet
        fields = ['content']
