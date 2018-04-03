from django.urls import path
from post.views import PostList
from . import views

app_name = 'core'

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('profile/<int:profile_id>/', views.index, name='profile_page'),
    path('login/', views.Login.as_view(), name='login_page'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register_page'),
]
