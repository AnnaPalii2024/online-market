from django.urls import path, include
from store.views.categories import CategoryViewSet
from store.views.products import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
urlpatterns = [
    path('', include(router.urls)),
]