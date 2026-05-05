from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.vendors.models import VendorStore


@admin.register(VendorStore)
class VendorStoreAdmin(ModelAdmin):
    list_display = ["name", "platform", "shop_id", "owner", "is_active", "created_at"]
    list_filter = ["platform", "is_active"]
    search_fields = ["name", "shop_id"]
    list_editable = ["is_active"]

    # Readonly fields
    readonly_fields = ["created_at", "updated_at", "owner"]
    
    # fieldsets
    fieldsets = (
        ("Informasi Toko", {
            "fields": ("name", "owner"),
        }),
        ("Detail Platform", {
            "fields": ("platform", "shop_id", "shop_url"),
        }),
        ("Status", {
            "fields": ("is_active",),
        }),
        ("Informasi Sistem", {
            "classes": ("collapse"),
            "fields": ("created_at", "updated_at"),
        }),
    )
