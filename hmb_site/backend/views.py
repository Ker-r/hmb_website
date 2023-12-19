from django.shortcuts import render
from django.views import View
from .models import Product


def home(request):
    return render(request, 'hmb_site/home.html')


def blog(request):
    return render(request, 'hmb_site/blog.html')


def contact(request):
    return render(request, 'hmb_site/contact.html')


class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, 'hmb_site/category.html', locals())


class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, 'hmb_site/category.html', locals())


class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'hmb_site/product_detail.html', locals())
