from django.db import models
from django.utils.timezone import now

# Create your models here.


class Product(models.Model):
    """Модель описывающая товар на сайте"""
    # название товара
    title = models.CharField(max_length=64, verbose_name='Название')
    # изображение товара
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    # описание товара
    description = models.TextField(max_length=256, blank=True, verbose_name='Описание')
    # цена товара
    price = models.FloatField(verbose_name='Цена')
    # дата создания страницы товара
    time_create = models.DateTimeField(default=now, blank=True, verbose_name='Дата создания')
    # дата обновления страницы товара
    time_update = models.DateTimeField(default=now, blank=True, verbose_name='Дата изменения')
    # опубликован ли товар на сайте
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    # внешний ключ
    sale = models.ForeignKey('Sale', on_delete=models.SET_NULL, null=True, default=None)

    # эта ф-ия нужна чтобы в админ панели отображалось название продукта, а не Object(0) и т. п.
    def __str__(self):
        return self.title


class Sale(models.Model):
    """Модель описывающая кол-во продаж того или иного товара"""
    # название товара(это просто нужно для обучения работы с БД!)
    title = models.CharField(max_length=64, verbose_name='Название', default='')
    # само кол-во продаж
    sales = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}: {self.sales}'