from django.contrib import admin
from electronics.models import Supplier, Product


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'network_level', 'country', 'city', 'debt_to_supplier', 'created_at')
    list_filter = ('network_level', 'title', 'product', 'country',)
    search_fields = ('network_level', 'product', 'country')
    actions = ["clear_debt"]

    @admin.action(description="Clearing the debt to the supplier")
    def clear_debt(self, request, queryset):
        queryset.update(debt_to_supplier=0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'product_model', 'launch_date')
