from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product, ProductCategory


def main(request):
    return render(request, 'mainapp/index.html', context={'user': request.user})


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    basket = request.user.basket.all()

    if pk:
        if pk == '0':
            category = {'name': 'Все'}
            product_list = Product.objects.all()
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            product_list = Product.objects.filter(category=category.id)
        context = {
            'title': 'Продукты',
            'products': product_list,
            'links_menu': links_menu,
            'category': category,
            'basket': basket,
        }
    else:
        product_list = Product.objects.all()
        context = {
            'title': 'Продукты',
            'products': product_list,
            'links_menu': links_menu,
            'basket': basket,
        }

    return render(request, 'mainapp/products_list.html', context)
    # else:
    #     product_list = Product.objects.all()
    #
    #     hot_product = get_hot_product()
    #     same_products = get_same_products(hot_product)
    #
    #     context = {
    #         'title': 'Продукты',
    #         'links_menu': links_menu,
    #         'hot_product': hot_product,
    #         'same_products': same_products,
    #     }
    #     return render(request, 'mainapp/products.html', context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')
