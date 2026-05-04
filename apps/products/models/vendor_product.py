from django.db import models
from apps.vendors.models.vendor_store import VendorStore


class VendorProduct(models.Model):
    """
    Menyimpan data produk dari toko vendor.
    Satu baris = satu produk vendor.
    """

    PRIORITY_CHOICES = [
        ("high", "Tinggi"),
        ("medium", "Sedang"),
        ("low", "Rendah"),
    ]

    store = models.ForeignKey(VendorStore, on_delete=models.CASCADE, related_name="products", verbose_name="Toko Vendor")
    item_id = models.CharField(max_length=50, db_index=True, verbose_name="Item ID")
    name = models.CharField(max_length=500, verbose_name="Nama Produk")
    product_url = models.URLField(verbose_name="URL Produk")
    description = models.TextField(blank=True, verbose_name="Deskripsi")
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="medium", verbose_name="Prioritas", help_text="Menentukan seberapa sering produk ini dicek harganya")
    is_active = models.BooleanField(default=True, verbose_name="Aktif", help_text="Nonaktifkan untuk berhenti memantau produk ini")
    last_checked = models.DateTimeField(null=True, blank=True, verbose_name="Terakhir Dicek")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Produk Vendor"
        verbose_name_plural = "Produk Vendor"
        ordering = ["-updated_at"]
        unique_together = ["store", "item_id"]

    def __str__(self):
        return f"{self.name} — {self.store.name}"
    