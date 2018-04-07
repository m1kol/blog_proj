from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.PostList.as_view(), name="list_posts"),
    path('<int:post_id>/', views.PostDetail.as_view(), name='show_post'),
    # path('/<int:post_id>/<slug:slug>/', views.show_post, name="show_post(slug)"),
    path('create/', login_required(views.PostCreate.as_view()), name='create_post'),
    path('<int:post_id>/edit', login_required(views.PostEdit.as_view()), name='edit_post'),
]