from django.shortcuts import render, get_object_or_404
from post.models import Post


def list_posts(requests):

    posts = Post.objects.all()
    context = {
        "posts": posts,
    }

    return render(requests, "post/list_posts.html", context)


def show_post(request, post_id):

    post = get_object_or_404(Post, id=post_id)
    context = {
        "post": post,
    }

    return render(request, "post/post_detail.html", context)
