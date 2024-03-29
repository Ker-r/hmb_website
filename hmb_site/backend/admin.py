from django.contrib import admin
from .models import Product, News


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'title', 'price', 'category',)
    # Добавляем интерфейс для поиска по названию и по типу товара
    search_fields = ('title', 'category', )
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка
    empty_value_display = '-пусто-'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)
    search_fields = ('title',)
    empty_value_display = '-пусто-'
