from django.db import models

from blog import settings
from post.models import Post


class Like(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="likes", on_delete=models.CASCADE)
    to_post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Likes"
        verbose_name = 'Like'
