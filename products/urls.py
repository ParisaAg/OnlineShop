from django.urls import path,include
from .views import ProductsListView,ProductDetailView,CommentCreateView

urlpatterns = [
    path('',ProductsListView.as_view(),name='product_list'),
    path('<int:pk>/',ProductDetailView.as_view(),name='product_detail'),
    path('comment/<int:product_id>/',CommentCreateView.as_view(),name='comment_create'),
]
