from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import VendorProduct, ProductVariant


class ProductVariantInline(TabularInline):
    """
    Menampilkan variasi produk langsung di dalam halaman produk.
    Tidak perlu buka halaman terpisah untuk lihat variasinya.
    """
    model = ProductVariant
    extra = 0
    fields = ["name", "variant_id", "price", "stock", "sku", "is_active"]


@admin.register(VendorProduct)
class VendorProductAdmin(ModelAdmin):
    list_display = ["name", "store", "priority", "is_active", "last_checked"]
    list_filter = ["store", "priority", "is_active"]
    search_fields = ["name", "item_id"]
    list_editable = ["priority", "is_active"]
    inlines = [ProductVariantInline]
