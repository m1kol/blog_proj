from django.db import models
from blog import settings
from categories.models import Category


class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts",
                               verbose_name="Author",
                               on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categories")
    title = models.CharField(max_length=255, null=False, verbose_name="Title")
    text = models.TextField(blank=False, verbose_name="Content")
    likes_count = models.PositiveIntegerField(default=0, verbose_name="Number of likes")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation")
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'Post'
        verbose_name_plural = u'Posts'
