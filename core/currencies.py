# Kode mata uang ISO 4217 yang didukung
CURRENCY_CHOICES = [
    ("IDR", "Indonesian Rupiah"),
    ("MYR", "Malaysian Ringgit"),
    ("THB", "Thai Baht"),
    ("PHP", "Philippine Peso"),
    ("SGD", "Singapore Dollar"),
    ("USD", "US Dollar"),
]


# Mapping kode mata uang ke simbolnya
CURRENCY_SYMBOLS = {
    "IDR": "Rp",
    "MYR": "RM",
    "THB": "฿",
    "PHP": "₱",
    "SGD": "S$",
    "USD": "$",
}


def get_currency_symbol(currency_code: str) -> str:
    """
    Mengembalikan simbol mata uang berdasarkan kode ISO 4217.
    Jika kode tidak ditemukan, kembalikan kode itu sendiri.

    Contoh:
        get_currency_symbol("IDR") → "Rp"
        get_currency_symbol("USD") → "$"
        get_currency_symbol("XXX") → "XXX"
    """
    return CURRENCY_SYMBOLS.get(currency_code, currency_code)