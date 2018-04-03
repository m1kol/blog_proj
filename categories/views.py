from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from categories.models import Category
from post.models import Post


class ListCategories(ListView):

    model = Category
    context_object_name = 'categories'
    template_name = 'categories/category_list.html'


def list_categories(request):

    categories = Category.objects.all()
    context = {
        "categories": categories,
    }

    return render(request, "categories/category_list.html", context)


class CategoryDetail(DetailView):

    model = Category
    context_object_name = 'category'
    pk_url_kwarg = 'category_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['posts'] = Post.objects.filter(id=self.kwargs['category_id'])
        return context


def category_detail(request, category_id):

    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.all().filter(id=category_id)
    context = {
        "category": category,
        "posts": posts
    }

    return render(request, "categories/category_detail.html", context)

