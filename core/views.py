from django.shortcuts import render, get_object_or_404
from .models import User
from post.models import Post


def login(request):

    return render(request, "core/login_page.html")


def register(request):

    return render(request, "core/registrations_page.html")


def index(request, profile_id):

    user = get_object_or_404(User, id=profile_id)
    posts = Post.objects.all().filter(author_id=user.id)

    context = {
        "user": user,
        "posts": posts,
    }

    return render(request, "core/profile_page.html", context)
