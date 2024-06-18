from django.shortcuts import render
from django.views import generic
from .models import Product
# Create your views here.

class ProductsListView(generic.ListView):
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'products'

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'products'