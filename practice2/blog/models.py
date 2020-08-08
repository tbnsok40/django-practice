from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]


class Comment(models.Model):
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
