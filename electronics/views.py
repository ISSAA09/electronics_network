from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny

from electronics.filter import SupplierFilter
from electronics.models import Supplier, Product
from electronics.serializers import (
    SupplierUpdateSerializer,
    SupplierSerializer,
    ProductSerializer,
)
from users.permissions import IsOwner, IsAdmin, IsActive


class ProductViewSet(viewsets.ModelViewSet):
    """
    Контроллер для модели Продуктов
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):

        if self.action == "retrieve":
            permission_classes = [IsAuthenticated, IsActive]
        elif self.action == "create":
            permission_classes = [IsAuthenticated, IsActive]
        elif self.action in ["update", "partial_update", "destroy"]:
            permission_classes = [IsAuthenticated, IsOwner | IsAdmin, IsActive]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        supplier = serializer.save()
        supplier.author = self.request.user
        supplier.save()


class SupplierViewSet(viewsets.ModelViewSet):
    """
    Контроллер для модели Поставщик
    """

    queryset = Supplier.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupplierFilter

    def get_serializer_class(self):
        if self.action in ["update", "partial_update"]:
            return SupplierUpdateSerializer
        else:
            return SupplierSerializer

    def get_permissions(self):
        if self.action == "retrieve":
            permission_classes = [IsAuthenticated, IsActive]
        elif self.action == "create":
            permission_classes = [IsAuthenticated, IsActive]
        elif self.action in ["update", "partial_update", "destroy"]:
            permission_classes = [IsAuthenticated, IsOwner | IsAdmin, IsActive]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        supplier = serializer.save()
        supplier.author = self.request.user
        supplier.save()
