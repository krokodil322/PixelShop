from shop.models import *


# В python shell неудобно прописывать CRUD операции :((
# Поэтому напишу в начале тут, а потом CTRL + C CTRL + V :))
# Этот скрипт создаёт объекты модели Sale по объектам модели Product
# а также расставляет foreign key объектам модели Product

# products = Product.objects.all()
# for product in products:
#     sale_obj = Sale(
#         title=product.title,
#         sales=0,
#     )
#     sale_obj.save()
#     product.sale_id = sale_obj.pk
#     product.save()




