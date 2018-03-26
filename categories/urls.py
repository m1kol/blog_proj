from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.list_categories, name="list_categories"),
    path('<int:category_id>/', views.category_detail, name="category_detail"),
    # path('<int:category_id>/<slug:slug>/', views.category_detail, name="category_detail(slug)"),
]