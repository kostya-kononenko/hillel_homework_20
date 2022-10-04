from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    full_description = models.TextField()
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text_comment = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']