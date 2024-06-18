from django.urls import path,include
from .views import ProductsListView,ProductDetailView

urlpatterns = [
    path('',ProductsListView.as_view(),name='product_list'),
    path('<int:pk>/',ProductDetailView.as_view(),name='product_detail'),
]
