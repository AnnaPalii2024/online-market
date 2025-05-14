from django.urls import path, include
from rest_framework.routers import DefaultRouter

from store.views.address import AddressViewSet
from store.views.categories import CategoryViewSet
from store.views.customers import CustomerListCreateView, CustomerDetailUpdateDeleteView
from store.views.orders import (
    OrderListCreateView,
    OrderDetailUpdateDeleteView,
    OrderItemListCreateView,
    OrderItemDetailUpdateDeleteView
)
from store.views.products import (
    ProductListCreateView,
    ProductRetrieveUpdateDeleteView,
    ProductDetailListCreateView,
    ProductDetailRetrieveUpdateDeleteView
)
from store.views.suppliers import SupplierViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'addresses', AddressViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('products/', ProductListCreateView.as_view()),
    path('products/<int:pk>/', ProductRetrieveUpdateDeleteView.as_view()),
    path('product-details/', ProductDetailListCreateView.as_view()),
    path('product-details/<int:pk>/', ProductDetailRetrieveUpdateDeleteView.as_view()),
    path('customers/', CustomerListCreateView.as_view()),
    path('customers/<int:pk>/', CustomerDetailUpdateDeleteView.as_view()),
    path('orders/', OrderListCreateView.as_view()),
    path('orders/<int:pk>/', OrderDetailUpdateDeleteView.as_view()),
    path('order-items/', OrderItemListCreateView.as_view()),
    path('order-items/<int:pk>/', OrderItemDetailUpdateDeleteView.as_view()),
]
