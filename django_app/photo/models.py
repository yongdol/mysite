from django.db import models
from django.conf import settings


class Album(models.Model):
    title = models.CharField(max_length=20)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True)
    description = models.CharField(max_length=100)


class Photo(models.Model):
    Album = models.ForeignKey(Album)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True)
    img = models.ImageField(upload_to='photo')

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='PhotoLike', related_name='photo_set_like_users')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='PhotoDisLike', related_name='photo_set_dislike_users')


class PhotoLike(models.Model):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)


class PhotoDisLike(models.Model):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)
