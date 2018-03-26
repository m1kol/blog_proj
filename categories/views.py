from django.shortcuts import render, get_object_or_404
from categories.models import Category
from post.models import Post


def list_categories(request):

    categories = Category.objects.all()
    context = {
        "categories": categories,
    }

    return render(request, "categories/list_categories.html", context)


def category_detail(request, category_id):

    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.all().filter(id=category_id)
    context = {
        "category": category,
        "posts": posts
    }

    return render(request, "categories/category_detail.html", context)

