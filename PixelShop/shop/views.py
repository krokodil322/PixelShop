from .models import *
from .forms import *
from .services import index_service

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound


def index(request):
    """Функция которая отображает главную страницу сайта"""

    # дёргаем ключ сортировки из формы
    # по умолчанию стоит absent, что значит
    # вывести всё без каких-либо сортировок
    sort_key = request.POST.get('sort_key', 'absent')
    # использвуем ф-ию из файла service.py
    products = index_service(sort_key)

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
    # тут берём объект продаж
    sale_obj = Sale.objects.filter(id=product.sale_id)[0]

    # словарик с передаваемыми данными
    context = {
        'product': product,
        'sales': sale_obj.sales
    }
    return render(request, 'shop/card_product.html', context)


def add_product(request):
    """
    Функция которая добавляет данные в БД при помощи обычной формы на сайте
    Есть большой потенциал к её изменению.
    """

    # если в форме нажали кнопку добавить сработает эта ветвь:
    if request.method == 'POST':
        # создаём объект класса формы по пришедшим из request данным
        form = AddProductForm(request.POST, request.FILES)
        # если в пришедших данных из формы нет ошибок то:
        if form.is_valid():
            # почему тут не form.save()?
            # штука в том, что в новоприбывшие данные формы
            # нужно добавить sale_id, а через объект формы
            # это не получается, поэтому дёргаем всё из формы :((
            title = form.cleaned_data.get('title')
            image = form.cleaned_data.get('image')
            description = form.cleaned_data.get('description')
            price = form.cleaned_data.get('price')
            is_published = form.cleaned_data.get('is_published')

            product = Product(
                title=title,
                image=image,
                description=description,
                price=price,
                is_published=is_published
            )
            # сразу создаём новый объект модели продаж Sale
            # чтобы подсчитывать кол-во продаж на сайте
            sale = Sale(title=title)
            sale.save()
            # создаём связь между объектом модели Sale и Product'а
            product.sale_id = sale.pk
            product.save()

            return redirect('home')
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


def buy_product(request, product_fk: int):
    """Функция которая симулирует покупку на сайтике"""

    # хапаем объект из таблицы Sales по foreign key product'а
    sale_obj = Sale.objects.filter(id=product_fk)[0]

    # инкрементируем атрибут и сохраняем изменения
    sale_obj.sales += 1
    sale_obj.save()

    # дёргаем объектик по которому добавляли продажу и
    # переадресуем обратно в карточку товара
    product = Product.objects.filter(sale_id=product_fk)[0]

    context = {
        'product': product,
    }
    return redirect(f'/card_product/{product.id}/')


def page_not_found(request, exception):
    """Если страницу по URL'у не находит, то эта ф-ия перехватывает управление"""
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')