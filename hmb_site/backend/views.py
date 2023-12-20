from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Product, Cart
from django.db.models import Q


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


def add_to_cart(request):
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(product=product).save()
    return redirect('/cart')


def show_cart(request):
    cart = Cart.objects.all()
    amount = 0
    for p in cart:
        value = p.quantity * p.product.price
        amount = amount + value
    totalamount = amount + 100
    return render(request, 'hmb_site/add_to_cart.html', locals())


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(product=prod_id)
        c.quantity += 1
        c.save()
        cart = Cart.objects.all()
        amount = 0
        for p in cart:
            value = p.quantity * p.product.price
            amount = amount + value
        totalamount = amount + 100
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(product=prod_id)
        c.quantity -= 1
        c.save()
        cart = Cart.objects.all()
        amount = 0
        for p in cart:
            value = p.quantity * p.product.price
            amount = amount + value
        totalamount = amount + 100
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(product=prod_id)
        c.delete()
        cart = Cart.objects.all()
        amount = 0
        for p in cart:
            value = p.quantity * p.product.price
            amount = amount + value
        totalamount = amount + 100
        data = {
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)
