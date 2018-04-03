from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.ListCategories.as_view(), name="list_categories"),
    path('<int:category_id>/', views.CategoryDetail.as_view(), name="category_detail"),
    # path('<int:category_id>/<slug:slug>/', views.category_detail, name="category_detail(slug)"),
]
