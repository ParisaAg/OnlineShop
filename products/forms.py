from django import forms
from .models import Product,Comment



class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['text','stars',]