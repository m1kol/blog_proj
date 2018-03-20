from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):

    list_display = ("author", "post", "text",)
