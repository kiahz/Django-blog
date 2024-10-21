from articles.models import Article
from . import models
from django import forms


class create_article(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title','slug','body','image']

