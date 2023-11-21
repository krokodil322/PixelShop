from .models import *
from .forms import *

from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    """Функция которая отображает главную страницу сайта"""

    # тут мы получаем список всех продектов из БДшки
    products = Product.objects.all()
    # словарик с передаваемыми данными
    context = {
        'header': 'Магазик',
        'title': 'Магазик пиксельных минералов!',
        'products': products,
    }
    return render(request, 'shop/index.html', context)


def card_product(request, product_id: int):
    """Функция которая отображает карточку товара по его id"""

    # тут мы хапаем конкретный товар по IDишнику который приходит из html-документа
    product = Product.objects.filter(id=product_id)[0]
    # словарик с передаваемыми данными
    context = {
        'header': product.title,
        'product': product,
    }
    return render(request, 'shop/card_product.html', context)


def add_product(request):
    """Функция которая добавляет данные в БД при помощи обычной формы на сайте"""

    # если в форме нажали кнопку добавить сработает эта ветвь:
    if request.method == 'POST':
        # создаём объект класса формы по пришедшим из request данным
        form = AddProductForm(request.POST, request.FILES)
        # если в пришедших данных из формы нет ошибок то:
        if form.is_valid():
            # через форму в Django можно сохранить прямо в БД!
            form.save()
            return redirect('/')
    # если просто вывести форму на экран
    form = AddProductForm()
    # словарик с передаваемыми данными
    context = {
        'header': 'Добавление',
        'title': 'Тут ты можешь добавить новый товар!',
        'form': form,
    }
    return render(request, 'shop/add_product.html', context)


def change_product(request, product_id: int):
    """Функция изменяющая данные товара"""

    # Хапаем товар из бдшке по указанной модели и id товара в бд
    product = get_object_or_404(Product, pk=product_id)
    # эта ветка запускается когда ты отправляешь изменённую фрму
    if request.method == 'POST':
        # по каким то причинам отказывается фурычить без атрибута instance
        form = AddProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            # после сохра редиректим на карточку товара который изменили
            return redirect(f'/card_product/{product_id}')
    # эта часть срабатывает самой первой
    # создаем объект формы и с помощью атра instance заранее её заполняем
    form = AddProductForm(instance=product)
    # словарик с передаваемыми данными
    context = {
        'header': 'Изменение',
        'title': 'В этой карточке ты можешь менять значение товаров!',
        'form': form,
        'id': product_id,
    }
    return render(request, 'shop/change_product.html', context)


def delete_product(request, product_id: int):
    """Функция удаляющая указанный в id товар из БД"""

    # удаляем товар по указанному id из БД
    Product.objects.filter(id=product_id).delete()
    # редиректим на главную
    return redirect('home')