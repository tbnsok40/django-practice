from django.db import models
from django.conf import settings
from django import forms


class Blog(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name="author_user")

    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]


class Comment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name="author_user2")  # related naems의 충돌

    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    body = models.CharField('re', max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body


class ReComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    body = models.CharField('re-reply', max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body
