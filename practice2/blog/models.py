from django.db import models

# Create your models here.


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
    body = models.CharField('댓글', max_length=150)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body


class ReComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    body = models.CharField('대댓글', max_length=150)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body
