from django.shortcuts import render, redirect
from django.views import View
from .models import Product, Category
from django.core import serializers


class HomePage(View):
    def get(self, request, category_slug=None):
        products = Product.objects.all()
        category = Category.objects.all()
        if category_slug:
            cat = Category.objects.get(slug=category_slug)
            products = products.filter(category=cat)
        return render(request, 'products/home.html', {'products': products, 'category': category})


class ProductDetailView(View):
    def get(self, request, product_slug):
        product = Product.objects.get(slug=product_slug)
        return render(request, 'products/detail.html', {'product': product})

