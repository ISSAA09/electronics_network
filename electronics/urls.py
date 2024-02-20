from django.urls import include, path
from rest_framework.routers import DefaultRouter
from electronics.views import SupplierViewSet, ProductViewSet
from electronics.apps import ElectronicsConfig

app_name = ElectronicsConfig.name

electronics_router = DefaultRouter()
electronics_router.register(r"supplier", SupplierViewSet, basename="supplier")

product_router = DefaultRouter()
product_router.register(r"product", ProductViewSet, basename="product")

urlpatterns = [
    path("", include(electronics_router.urls)),
    path("", include(product_router.urls)),
]
