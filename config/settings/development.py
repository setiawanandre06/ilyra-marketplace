from .base import *
from decouple import config

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0", "192.168.1.4"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST", default="localhost"),
        "PORT": config("DB_PORT", default="5432"),
    }
}

# Redis & Celery
CELERY_BROKER_URL = config("REDIS_URL", default="redis://localhost:6379/0")
