from django.shortcuts import render,get_object_or_404,reverse
from django.views import generic
from .forms import CommentForm
from .models import Product,Comment
# Create your views here.

class ProductsListView(generic.ListView):
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'products'

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['comment_form']= CommentForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class=CommentForm

    def form_valid(self, form):
        obj=form.save(commit=False)
        obj.author=self.request.user
        product_id=int(self.kwargs['product_id'])
        product=get_object_or_404(Product,id=product_id)
        obj.product=product
        return super().form_valid(form)