from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from comment.views import CommentCreate
from like.views import LikeCreate

app_name = 'post'

urlpatterns = [
    path('', views.PostList.as_view(), name="list_posts"),
    path('<int:post_id>/', views.PostDetail.as_view(), name='show_post'),
    # path('/<int:post_id>/<slug:slug>/', views.show_post, name="show_post(slug)"),
    path('create/', login_required(views.PostCreate.as_view()), name='create_post'),
    path('<int:post_id>/edit', login_required(views.PostEdit.as_view()), name='edit_post'),
    path('<int:post_id>/comment-post', login_required(CommentCreate.as_view()), name='post_comments'),
    path('<int:post_id>/like', login_required(LikeCreate.as_view()), name='post_like'),
    path('<int:post_id>/comments', CommentCreate.as_view(), name='post_comments'),
]