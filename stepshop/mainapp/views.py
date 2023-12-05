from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
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


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []


def index(request):
    title = "Главная"

    _products = Product.objects.all()

    basket = get_basket(request.user)

    context = get_data(title=title, prods=_products, basket=basket)

    return render(request, 'index.html', context)


def about(request):
    title = "О нас"

    basket = get_basket(request.user)

    context = get_data(title=title, basket=basket)

    return render(request, 'about.html', context)


def contacts(request):
    title = "Контакты"

    basket = get_basket(request.user)

    context = get_data(title=title, basket=basket)

    return render(request, 'contacts.html', context)


def product(request, pk):
    title = "Покупка продукта"
    prod = Product.objects.get(pk=pk)
    same_prods = Product.objects.filter(category=prod.category).exclude(pk=pk)

    basket = get_basket(request.user)

    context = get_data(title=title, prod=prod, same_prods=same_prods, basket=basket)

    return render(request, 'product.html', context)


def products(request, pk=None):
    title = "Каталог продуктов"

    # _products = Product.objects.all()
    _products = Product.objects.order_by('price')
    context = {}

    basket = get_basket(request.user)

    if pk is not None:
        category = get_object_or_404(Category, pk=pk)
        _products = Product.objects.filter(category__pk=pk).order_by('price')
        context = get_data(category=category)

    context = get_data(title=title, prods=_products, basket=basket, **context)

    return render(request, 'products.html', context)

