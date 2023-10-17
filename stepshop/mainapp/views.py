from django.shortcuts import render


def index(request):
    title = "Главная"

    links_menu = [
        {'link': 'index', 'name': 'HOME'},
        {'link': 'products:index', 'name': 'PRODUCTS'},
        {'link': 'about', 'name': 'ABOUT US'},
        {'link': 'contacts', 'name': 'CONTACT US'}
    ]

    context = {
        'title': title,
        'links_menu': links_menu,

    }

    return render(request, 'index.html', context)


def about(request):
    title = "О нас"

    context = {'title': title}

    return render(request, 'about.html', context)


def contacts(request):
    title = "Контакты"

    context = {'title': title}

    return render(request, 'contacts.html', context)


def product(request):
    title = "Покупка продукта"

    context = {'title': title}

    return render(request, 'product.html', context)


def products(request):
    title = "Каталог продуктов"

    context = {'title': title}

    return render(request, 'products.html', context)

