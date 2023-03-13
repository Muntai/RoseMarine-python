from django.shortcuts import render


def index(request):
    data = {
        'title': 'Ресторан «RoseMarine» - ресторан в Кривому Розі | Банкети | Весілля | Дні народження - ᐉ Ресторан «RoseMarine» ᐉ Весілля, корпоративи, банкети, дні народження.',
        'metatitle': 'Ресторан «RoseMarine» - ресторан в Кривому Розі | Банкети | Весілля | Дні народження - ᐉ Ресторан «RoseMarine» ᐉ Весілля, корпоративи, банкети, дні народження.',
        'description': 'Ресторан «RoseMarine» ᐉ Всі страви готуються виключно з якісних локальних продуктів ᐉ Якісна їжа. ᐉ вул. Співдружності 77а'
    }

    return render(request, 'main/index.html', data)
