from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def get_data(**kwargs):
    links_menu = [
        {'link': 'index', 'name': 'HOME'},
        {'link': 'products:index', 'name': 'PRODUCTS'},
        {'link': 'about', 'name': 'ABOUT US'},
        {'link': 'contacts', 'name': 'CONTACT US'}
    ]

    categories = Category.objects.all()

    context = {
        'links_menu': links_menu,
        'categories': categories,
    }
    context.update(**kwargs)
    return context


def index(request):
    title = "Главная"

    _products = Product.objects.all()

    context = get_data(title=title, prods=_products)

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


def products(request, pk=None):
    title = "Каталог продуктов"

    # _products = Product.objects.all()
    _products = Product.objects.order_by('price')
    context = {}

    if pk is not None:
        category = get_object_or_404(Category, pk=pk)
        _products = Product.objects.filter(category__pk=pk).order_by('price')
        context = get_data(category=category)

    context = get_data(title=title, prods=_products, **context)

    return render(request, 'products.html', context)

