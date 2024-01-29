from django import forms
from .models import Product


class SizeAddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('size', )
