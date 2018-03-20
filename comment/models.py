from django.db import models

from blog import settings
from post.models import Post


class Comment(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comments",
                               on_delete=models.CASCADE,
                               verbose_name="Author")
    post = models.ForeignKey(Post, related_name="comments",
                             on_delete=models.CASCADE,
                             verbose_name="Commented post")
    text = models.TextField(verbose_name="Comment text")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Comments"
        verbose_name = "Comment"
