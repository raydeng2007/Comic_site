
from django.db import models
from django.contrib.auth.models import User


class Series(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)


class Episode(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name='episodes')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='episodes')


class Comment(models.Model):
    message = models.TextField(max_length=4000)
    episodes = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
