from django.shortcuts import render, redirect
from .models import Category, Product




def kuhnya(request):
    data = {
        'title': 'Меню Кухня - ᐉ Ресторан «RoseMarine» ᐉ Весілля, корпоративи, банкети, дні народження.',
        'metatitle': 'Меню Кухня - ᐉ Ресторан «RoseMarine» ᐉ Весілля, корпоративи, банкети, дні народження.',
        'description': 'Ресторан «RoseMarine» ᐉ Всі страви готуються виключно з якісних локальних продуктів ᐉ Якісна їжа. ᐉ вул. Співдружності 77а'

    }
    return render(request, 'kuhnya/kuhnya.html', data)


def pershi_stravi(request):
    data = {
        'title': 'Перші страви - ᐉ Ресторан «RoseMarine» ᐉ Весілля, корпоративи, банкети, дні народження.',
        'metatitle': 'Перші страви - ᐉ Ресторан «RoseMarine» ᐉ Весілля, корпоративи, банкети, дні народження.',
        'description': 'Ресторан «RoseMarine» ᐉ Всі страви готуються виключно з якісних локальних продуктів ᐉ Якісна їжа. ᐉ вул. Співдружності 77а'
    }
    return render(request,'kuhnya/pershi_stravi.html', data)



def pershi_stravi(request):
    products = Product.objects.filter(category='8')
    return render(request, 'kuhnya/pershi_stravi.html', {'products': products})
