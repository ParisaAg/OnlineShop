from django.contrib import admin
from .models import Product,Comment
# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    fields =  ['author','text','status','stars',]
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','status',]
    inlines = [CommentInline,]


@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product','author','text','status','stars',]

