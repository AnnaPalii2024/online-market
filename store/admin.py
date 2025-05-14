
from django.contrib import admin
from store.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в списке записей
    list_display = ('name',)

    # Добавление поиска по полю 'name'
    search_fields = ('name',)

    # Сортировка записей по полю 'name' в алфавитном порядке
    ordering = ('name',)
