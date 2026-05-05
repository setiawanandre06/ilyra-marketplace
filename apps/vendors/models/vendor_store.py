from django.db import models
from django.contrib.auth.models import User


class VendorStore(models.Model):
    """
    Menyimpan data toko vendor yang dipantau.
    Satu baris = satu toko vendor.
    """

    PLATFORM_CHOICES = [
        ("shopee", "Shopee"),
        ("tokopedia", "Tokopedia"),
        ("tiktok", "TikTok Shop"),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vendor_stores", verbose_name="Pemilik")
    name = models.CharField(max_length=255, verbose_name="Nama Toko")
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, default="shopee", verbose_name="Platform", db_index=True)
    shop_id = models.CharField(max_length=50, db_index=True, verbose_name="Shop ID")
    shop_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="URL Toko")
    is_active = models.BooleanField(default=True, verbose_name="Aktif", db_index=True, help_text="Nonaktifkan untuk berhenti memantau semua produk toko ini")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Dibuat Pada")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Diupdate Pada")

    class Meta:
        verbose_name = "Toko Vendor"
        verbose_name_plural = "Toko Vendor"
        ordering = ["-updated_at"]
        unique_together = ["platform", "shop_id"]

    def __str__(self):
        return f"{self.name} ({self.get_platform_display()})"