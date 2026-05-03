from .base import *

SECRET_KEY = "django-insecure-ganti-ini-dengan-string-acak-untuk-development"

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Sementara pakai SQLite dulu, nanti ganti PostgreSQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}