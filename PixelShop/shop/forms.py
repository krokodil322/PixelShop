from django import forms
from .models import *


# 2 класса один из которых класс формы, а внутри это мета-класс
# который ссылается на класс-модель Product из БД
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title', 'image', 'description',
            'price', 'is_published',
        ]