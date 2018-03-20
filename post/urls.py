from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_posts, name="list_posts"),
    path('<int:post_id>/', views.show_post),
    # path('/<int: post_id>/<slug: slug>/', views.show_post, name="show_post(slug)"),
]