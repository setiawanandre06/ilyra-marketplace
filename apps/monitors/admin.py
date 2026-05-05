from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.monitors.models import PriceHistory


@admin.register(PriceHistory)
class PriceHistoryAdmin(ModelAdmin):
    list_display = ["product_display", "variant_display", "currency", "old_price", "new_price", "price_difference", "recorded_at"]
    list_filter = ["currency", "recorded_at"]
    search_fields = ["product__name", "variant__name"]
    readonly_fields = ["recorded_at"]
    
    # fieldsets
    fieldsets = (
        ("Informasi Produk", {
            "fields": ("product", "variant"),
        }),
        ("Informasi Harga", {
            "fields": ("currency", "old_price", "new_price", "price_difference"),
        }),
        ("Informasi Sistem", {
            "classes": ("collapse",),
            "fields": ("recorded_at",),
        }),
    )
    
    def product_display(self, obj):
        return obj.product.name
    product_display.short_description = "Produk"
    
    def variant_display(self, obj):
        return obj.variant.name if obj.variant else "-"
    variant_display.short_description = "Variasi"

    def has_add_permission(self, request):
        return False  # Riwayat harga tidak boleh ditambah manual

    def has_delete_permission(self, request, obj=None):
        return False  # Riwayat harga tidak boleh dihapus
