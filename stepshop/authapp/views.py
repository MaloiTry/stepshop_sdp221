from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

from mainapp.views import get_data
from .forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm


def login(request):
    title = 'Вход'
    login_form = ShopUserLoginForm(data=request.POST)

    if request.method == "POST" and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))

    context = get_data(title=title, login_form=login_form)
    # context = {
    #     'title': title,
    #     'login_form':  login_form,
    # }

    return render(request, 'auth/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    title = 'Регистрация'

    if request.method == "POST":
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    context = get_data(title=title, register_form=register_form)

    return render(request, 'auth/register.html', context)


def edit(request):
    title = 'Редактирование'

    if request.method == "POST":
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    context = get_data(title=title, edit_form=edit_form)

    return render(request, 'auth/edit.html', context)
