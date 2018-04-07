from django.shortcuts import get_object_or_404, reverse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from categories.models import Category
from .models import Post
from .forms import PostListForm


class PostDetail(generic.DetailView):

    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        categories = Category.objects.all().filter(id=kwargs["object"].pk)
        if categories.__len__() != 0:
            context['categories'] = categories
        return context


class PostList(generic.ListView):

    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'
    ordering = ("title",)
    search_term = None
    sort_term = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.form = None

    def dispatch(self, request, *args, **kwargs):
        self.form = PostListForm(self.request.GET)
        if self.form.is_valid():
            self.search_term = self.form.cleaned_data['search']
            self.sort_term = self.form.cleaned_data['sort']
        return super().dispatch(request, args, kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context['form'] = self.form
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_term:
            queryset = queryset.filter(title__icontains=self.search_term)
        if self.sort_term:
            queryset = queryset.order_by(self.sort_term)
        return queryset


class PostCreate(generic.CreateView):

    model = Post
    fields = ('title', 'text', 'categories', )
    template_name = 'post/post_create.html'

    def get_success_url(self):
        return reverse('post:show_post', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class PostEdit(generic.UpdateView):

    model = Post
    fields = ('title', 'text', 'categories',)
    template_name = 'post/post_edit.html'
    pk_url_kwarg = 'post_id'

    def get_success_url(self):
        return reverse('post:show_post', kwargs={'pk': self.object.pk})
