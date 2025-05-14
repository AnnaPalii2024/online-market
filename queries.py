import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_config.settings')
django.setup()


# TASK 1

# Вычислить общую стоимость всех продуктов в базе данных.


# from django.db.models import Sum, F
# from store.models import Product
#
# total_value = Product.objects.aggregate(
#     total_value=Sum(F('price') * F('quantity'))
# )['total_value']
#
#
# print(f"Общая стоимость всех продуктов: {total_value}")



# -------------------------------------------------------------------------------------------------------------

# TASK 2

# Вычислить среднюю цену продуктов для каждой категории


# from django.db.models import Avg
# from store.models import Product
#
# average_price_by_category = Product.objects.values('category__name').annotate(
#     average_price=Avg('price')
# ).order_by('category__name')
#
# for entry in average_price_by_category:
#     print(f"Категория: {entry['category__name']}, Средняя цена: {entry['average_price']}")
#


# -------------------------------------------------------------------------------------------------------------


# TASK 3

#  Найти самый дешевый и самый дорогой продукт.

# from django.db.models import Min, Max
# from store.models import Product
#
#
# cheapest_product = Product.objects.aggregate(
#     min_price=Min('price')
# )['min_price']
#
#
# most_expensive_product = Product.objects.aggregate(
#     max_price=Max('price')
# )['max_price']
#
#
# print(f"Самый дешевый продукт: {cheapest_product}")
# print(f"Самый дорогой продукт: {most_expensive_product}")



# -------------------------------------------------------------------------------------------------------------


# TASK 4

#  Вычислить количество заказов и общую стоимость заказов для каждого клиента.


# from django.db.models import Count, Sum, F
# from store.models import Order
#
# orders_summary_by_customer = Order.objects.values('customer__first_name', 'customer__last_name').annotate(
#     order_count=Count('id'),
#     total_spent=Sum(F('order_items__price') * F('order_items__quantity'))
# ).order_by('customer__last_name')
#
# for entry in orders_summary_by_customer:
#     print(f"Клиент: {entry['customer__first_name']} {entry['customer__last_name']}, Заказов: {entry['order_count']}, Общая сумма: {entry['total_spent']}")
#



# -------------------------------------------------------------------------------------------------------------


# TASK 5

#  Рассчитать общий вес всех продуктов для каждой категории.


# from django.db.models import Sum, F
# from store.models import Product
#
# total_weight_by_category = Product.objects.values('category__name').annotate(
#     total_weight=Sum(F('details__weight') * F('quantity'))
# ).order_by('category__name')
#
# for entry in total_weight_by_category:
#     print(f"Категория: {entry['category__name']}, Общий вес: {entry['total_weight']}")




# -------------------------------------------------------------------------------------------------------------


# TASK 6

# Вычислить количество различных продуктов, которые поставляет каждый поставщик.


# from django.db.models import Count
# from store.models import Product
#
# products_count_by_supplier = Product.objects.values('supplier__name').annotate(
#     product_count=Count('id')
# ).order_by('supplier__name')
#
# for entry in products_count_by_supplier:
#     print(f"Поставщик: {entry['supplier__name']}, Количество продуктов: {entry['product_count']}")



# -------------------------------------------------------------------------------------------------------------


# TASK 7

# Вычислить среднюю продолжительность жизни продуктов (в днях) на основе даты производства и срока годности.


# from django.db.models import Avg, F, ExpressionWrapper, fields
# from store.models import ProductDetail
# #
# average_lifetime = ProductDetail.objects.annotate(
#     lifetime=ExpressionWrapper(
#         F('expiration_date') - F('manufacturing_date'),
#         output_field=fields.DurationField()
#     )
# ).aggregate(average_lifetime=Avg('lifetime'))['average_lifetime']

# print(f"Средняя продолжительность жизни продуктов: {average_lifetime.days} дней")



# -------------------------------------------------------------------------------------------------------------


# TASK 8

# Рассчитать общую сумму всех заказов для каждого клиента.


# from django.db.models import Sum, F
# from store.models import Order, OrderItem
#
# total_spent_by_customer = Order.objects.values('customer__first_name', 'customer__last_name').annotate(
#     total_spent=Sum(F('order_items__price') * F('order_items__quantity'))
# ).order_by('customer__last_name')
#
# for entry in total_spent_by_customer:
#     print(f"Клиент: {entry['customer__first_name']} {entry['customer__last_name']}, Общая сумма заказов: {entry['total_spent']}")
#



# -------------------------------------------------------------------------------------------------------------


# TASK 9

# Сортировать список продуктов по их цене в порядке убывания.


# from store.models import Product
#
# # Сортировка по цене по убыванию
# products_descending = Product.objects.order_by('-price')
#
# print("Продукты по убыванию цены:")
# for product in products_descending:
#     print(f"{product.name}: {product.price}")



# -------------------------------------------------------------------------------------------------------------


# TASK 9

# Сортировать список заказов по их общей стоимости.


# from django.db.models import Sum, F
# from store.models import Order
#
# # Сортировка заказов по общей стоимости
# orders_by_total = Order.objects.annotate(
#     total=Sum(F('order_items__price') * F('order_items__quantity'))
# ).order_by('-total')
#
# print("Заказы по общей стоимости:")
# for order in orders_by_total:
#     print(f"Заказ {order.id}, Общая стоимость: {order.total}")
#



# -------------------------------------------------------------------------------------------------------------


# TASK 10

# Отсортировать список адресов сначала по стране, затем по городу.


# from store.models import Address
#
# # Сортировка по стране и городу
# addresses_sorted = Address.objects.order_by('country', 'city')
#
# print("Адреса по стране и городу:")
# for address in addresses_sorted:
#     print(f"{address.country}, {address.city}, {address.street}")



# -------------------------------------------------------------------------------------------------------------


# TASK 11

# Отсортировать список заказов по количеству позиций в каждом заказе.


# from django.db.models import Count
# from store.models import Order
#
# # Сортировка по количеству позиций заказа
# orders_by_item_count = Order.objects.annotate(
#     item_count=Count('order_items')
# ).order_by('-item_count')
#
# print("Заказы по количеству позиций:")
# for order in orders_by_item_count:
#     print(f"Заказ {order.id}, Количество позиций: {order.item_count}")



# -------------------------------------------------------------------------------------------------------------


# TASK 12

# Найти все заказы, сделанные за последний месяц.


# from django.utils import timezone
# from store.models import Order
#
# # Дата один месяц назад
# one_month_ago = timezone.now() - timezone.timedelta(days=30)
#
# # Заказы за последний месяц
# recent_orders = Order.objects.filter(order_date__gte=one_month_ago)
#
# print("Заказы за последний месяц:")
# for order in recent_orders:
#     print(f"Заказ {order.id}, Дата: {order.order_date}")




# -------------------------------------------------------------------------------------------------------------


# TASK 13

# Извлечь первые 5 продуктов из списка всех продуктов.


# from store.models import Product
#
# # Первые 5 продуктов
# first_five_products = Product.objects.all()[:5]
#
# print("Первые 5 продуктов:")
# for product in first_five_products:
#     print(f"{product.name}: {product.price}")


# -------------------------------------------------------------------------------------------------------------


# TASK 14

# Найти 10 самых дорогих продуктов.



# from store.models import Product
#
# # 10 самых дорогих продуктов
# top_ten_expensive_products = Product.objects.order_by('-price')[:10]
#
# print("10 самых дорогих продуктов:")
# for product in top_ten_expensive_products:
#     print(f"{product.name}: {product.price}")
#
