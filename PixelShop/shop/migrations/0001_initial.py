# Generated by Django 4.2.7 on 2023-11-17 13:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название')),
                ('description', models.TextField(blank=True, max_length=256, verbose_name='Описание')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('time_create', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('time_update', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Дата изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
        ),
    ]