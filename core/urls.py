from django.urls import path
from post.views import list_posts
from . import views

app_name = 'core'

urlpatterns = [
    path('', list_posts, name='home'),
    path('users/<int:profile_id>/', views.index, name='profile_page'),
    path('login/', views.login, name='login_page'),
    path('register/', views.register, name='register_page'),
]
