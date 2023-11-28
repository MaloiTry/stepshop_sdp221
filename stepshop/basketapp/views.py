from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import Basket, Product


def basket(request):
    if request.user.is_authenticated:
        user_basket = Basket.objects.filter(user=request.user)
        context = {'basket': user_basket}
        return render(request, 'basket/basket.html', context)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    user_basket = Basket.objects.filter(user=request.user, product=product).first()

    if not user_basket:
        user_basket = Basket(user=request.user, product=product)

    user_basket.quantity += 1
    user_basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request):
    pass
