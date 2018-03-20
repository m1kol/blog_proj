from django.urls import path
from post.views import list_posts
from . import views


urlpatterns = [
    path('', list_posts),
    path('<int:profile_id>/', views.index),
    path('login/', views.login),
    path('register/', views.register),
]
