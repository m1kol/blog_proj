from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=255, unique=True, verbose_name="Category name")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
