from django.db import models
from django.contrib.auth.models import User
class Article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(default='default.jpg',blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.title
    #ba in tag esme article k save krdim save mishe
    def snippet(self):
        return self.body[0:50]+'...'
    #baraye neshon ddn body ta saghfe 100 ta kalame
