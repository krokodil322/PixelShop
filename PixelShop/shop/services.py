from .models import *


# Файл в котором планируется бизнес-логика сайта PixelShop

def index_service(sort_key: str) -> list[tuple[Product, int]]:
    """Логика ф-ии index в файле views.py"""

    # SQL-запросы по соответствующим ключам сортировки
    sql_responses = {
        'absent': lambda: Product.objects.all(),
        'alphabet': lambda: Product.objects.all().order_by('title'),
        'alphabet-reverse': lambda: Product.objects.all().order_by('-title'),
        'price': lambda: Product.objects.all().order_by('price'),
        'price-reverse': lambda: Product.objects.all().order_by('-price'),
        'sales': lambda: Product.objects.all(),
        'sales-reverse': lambda: Product.objects.all(),
        'date': lambda: Product.objects.all().order_by('-time_create'),
        'date-reverse': lambda: Product.objects.all().order_by('time_create'),
    }

    products = []
    for product_obj in sql_responses[sort_key]():
        # некоторые новосозданные product'ы могут иметь sale_id=None
        # из-за чего извлечь объект Sale по FK не получается
        try:
            sale_obj = Sale.objects.filter(id=product_obj.sale_id)[0]
            products.append(
                (product_obj, sale_obj.sales)
            )
        except IndexError:
            continue

    # если сортировка ведётся во продажам
    if sort_key == 'sales':
        products.sort(key=lambda pair: pair[1])
    elif sort_key == 'sales-reverse':
        products.sort(key=lambda pair: pair[1])
        products.reverse()

    return products




