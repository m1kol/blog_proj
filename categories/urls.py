from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="list_categories"),
    path('<int:category_id>/', views.detail, name="category_detail"),
    # path('<int:category_id>/<slug:slug>/', views.category_detail, name="category_detail(slug)"),
]