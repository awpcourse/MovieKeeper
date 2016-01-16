from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Movie(models.Model):
    name = models.TextField(max_length=100)
    picture = models.ImageField(
        upload_to=get_image_path, blank=True, null=True)
    duration = models.TimeField()
    genre = models.TextField(max_length=50)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='user_comments')
    movie = models.ForeignKey(Movie, related_name='user_movies')
    dateTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['dateTime']


class WishList(models.Model):
    user = models.ForeignKey(User, related_name='user_wishlist')
    movie = models.ForeignKey(Movie, related_name='movie_wishlist')


class WatchList(models.Model):
    user = models.ForeignKey(User, related_name='user_watchlists')
    movie = models.ForeignKey(Movie, related_name='movie_movies')