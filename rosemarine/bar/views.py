from django.shortcuts import render, redirect
from .models import Category, Product


def bar(request):
    data = {
        'title': 'Меню Бар - ᐉ Ресторан «RoseMarine» ᐉ Весілля, корпоративи, банкети, дні народження.',
        'metatitle': 'Меню Бар - ᐉ Ресторан «RoseMarine» ᐉ Весілля, корпоративи, банкети, дні народження.',
        'description': 'Ресторан «RoseMarine» ᐉ Всі страви готуються виключно з якісних локальних продуктів ᐉ Якісна їжа. ᐉ вул. Співдружності 77а'
    }
    return render(request, 'bar/bar.html', data)


def firmovi_limonadi(request):
    data = {
        'title': 'Фірмові лимонади - ᐉ Ресторан «RoseMarine» ᐉ Весілля, корпоративи, банкети, дні народження.',
        'metatitle': 'Фірмові лимонади - ᐉ Ресторан «RoseMarine» ᐉ Весілля, корпоративи, банкети, дні народження.',
        'description': 'Ресторан «RoseMarine» ᐉ Всі страви готуються виключно з якісних локальних продуктів ᐉ Якісна їжа. ᐉ вул. Співдружності 77а'
    }
    return render(request, 'bar/firmovi_limonadi.html', data)


def firmovi_limonadi(request):
    products = Product.objects.filter(category='1')
    return render(request, 'bar/firmovi_limonadi.html', {'products': products})