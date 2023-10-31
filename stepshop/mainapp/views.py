from django.shortcuts import render
from .models import Product


def get_data(**kwargs):
    links_menu = [
        {'link': 'index', 'name': 'HOME'},
        {'link': 'products:index', 'name': 'PRODUCTS'},
        {'link': 'about', 'name': 'ABOUT US'},
        {'link': 'contacts', 'name': 'CONTACT US'}
    ]
    context = {
        'links_menu': links_menu,
    }
    context.update(**kwargs)
    return context


def index(request):
    title = "Главная"

    context = get_data(title=title)

    return render(request, 'index.html', context)


def about(request):
    title = "О нас"

    context = get_data(title=title)

    return render(request, 'about.html', context)


def contacts(request):
    title = "Контакты"

    context = get_data(title=title)

    return render(request, 'contacts.html', context)


def product(request, pk):
    title = "Покупка продукта"
    prod = Product.objects.get(pk=pk)

    context = get_data(title=title, prod=prod)

    return render(request, 'product.html', context)


def products(request):
    title = "Каталог продуктов"

    _products = Product.objects.all()

    context = get_data(title=title, prods=_products)

    return render(request, 'products.html', context)

