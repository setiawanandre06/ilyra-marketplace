from django.db import models
from apps.products.models import VendorProduct, ProductVariant
from core.currencies import CURRENCY_CHOICES, get_currency_symbol


class PriceHistory(models.Model):
    """
    Menyimpan riwayat perubahan harga produk vendor.
    Bisa merujuk ke produk saja (tanpa variasi)
    atau ke variasi spesifik (jika produk punya variasi).
    """

    product = models.ForeignKey(VendorProduct, on_delete=models.PROTECT, related_name="price_history", verbose_name="Produk")
    variant = models.ForeignKey(ProductVariant, on_delete=models.PROTECT, related_name="price_history", null=True, blank=True, verbose_name="Variasi", help_text="Kosong jika produk tidak memiliki variasi")

    # Mata Uang
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="IDR", verbose_name="Mata Uang")

    # Harga
    old_price = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Harga Lama")
    new_price = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Harga Baru")
    price_difference = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Selisih Harga", help_text="Positif = naik, Negatif = turun")

    # Status Aktif
    old_is_active = models.BooleanField(verbose_name="Status Aktif Lama")
    new_is_active = models.BooleanField(verbose_name="Status Aktif Baru")

    recorded_at = models.DateTimeField(auto_now_add=True, verbose_name="Dicatat Pada")
    
    class Meta:
        verbose_name = "Riwayat Harga"
        verbose_name_plural = "Riwayat Harga"
        ordering = ["-recorded_at"]

    def __str__(self):
        target = f"{self.product.name}"
        if self.variant:
            target += f" — {self.variant.name}"
        if self.price_difference > 0:
            arah = "naik"
        elif self.price_difference < 0:
            arah = "turun"
        else:
            arah = "tetap"
        symbol = get_currency_symbol(self.currency)
        return f"{target} ({arah} {symbol} {abs(self.price_difference):,.0f})"

    def save(self, *args, **kwargs):
        # Hitung selisih harga otomatis sebelum disimpan
        self.price_difference = self.new_price - self.old_price
        super().save(*args, **kwargs)