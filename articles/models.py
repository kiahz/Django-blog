from django.db import models

class Article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    # in add thumbnail
    # add in author
    def __str__(self):
        return self.title
    #ba in tag esme article k save krdim save mishe
    def snippet(self):
        return self.body[0:50]+' ...'
    #baraye neshon ddn body ta saghfe 100 ta kalame
