from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.vendors.models import VendorStore


@admin.register(VendorStore)
class VendorStoreAdmin(ModelAdmin):
    list_display = ["name", "platform", "shop_id", "owner", "is_active", "created_at"]
    list_filter = ["platform", "is_active"]
    search_fields = ["name", "shop_id"]
    list_editable = ["is_active"]
