from django.urls import path, include
from store.views.categories import CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('categories', CategoryViewSet)
urlpatterns = [
    path('', include(router.urls)),
]