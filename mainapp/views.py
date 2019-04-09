from django.shortcuts import render
from .models import Product, ProductCategory




def main(request):
    return render(request, 'mainapp/index.html')


def products(request, pk=None):
    product_list = Product.objects.all()

    return render(request, 'mainapp/products.html', context={'products': product_list})


def contacts(request):
    return render(request, 'mainapp/contacts.html')
