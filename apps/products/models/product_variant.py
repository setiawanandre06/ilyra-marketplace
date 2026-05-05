from django.db import models
from .vendor_product import VendorProduct


class ProductVariant(models.Model):
    """
    Menyimpan variasi dari setiap produk (ukuran, warna, dll).
    Satu produk bisa punya banyak variasi.
    Harga & stok disimpan di level variasi.
    """

    product = models.ForeignKey(VendorProduct, on_delete=models.CASCADE, related_name="variants", verbose_name="Produk Vendor")
    variant_id = models.CharField(max_length=50, db_index=True, verbose_name="Variant ID")
    name = models.CharField(max_length=255, verbose_name="Nama Variasi", help_text="Contoh: Merah - XL, Biru - M")
    price = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Harga")
    stock = models.IntegerField(default=0, verbose_name="Stok")
    sku = models.CharField(max_length=100, blank=True, verbose_name="SKU")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Variasi Produk"
        verbose_name_plural = "Variasi Produk"
        ordering = ["name"]
        unique_together = ["product", "variant_id"]

    def __str__(self):
        return f"{self.product.name} — {self.name}"