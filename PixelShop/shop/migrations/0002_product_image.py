# Generated by Django 4.2.7 on 2023-11-17 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='images', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
