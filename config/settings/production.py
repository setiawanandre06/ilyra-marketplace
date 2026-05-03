from .base import *

# Semua nilai sensitif wajib dari environment variable
# Akan diisi lengkap saat tahap deployment
SECRET_KEY = NotImplemented
DEBUG = False
ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        # Akan diisi saat setup PostgreSQL di server
    }
}