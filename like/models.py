from django.db import models

from blog import settings
from post.models import Post
from comment.models import Comment


class Like(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name="likes",
                               on_delete=models.CASCADE,
                               verbose_name="Author")
    post = models.ForeignKey(Post, related_name="likes",
                             on_delete=models.CASCADE,
                             verbose_name="Liked post")
    comment = models.ForeignKey(Comment, related_name="likes",
                                on_delete=models.CASCADE,
                                verbose_name="Liked comment")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Likes"
        verbose_name = 'Like'
