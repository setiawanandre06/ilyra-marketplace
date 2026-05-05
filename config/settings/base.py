from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = NotImplemented  # Di-override di development.py & production.py

DEBUG = False  # Default aman, di-override di development.py

ALLOWED_HOSTS = []

# Aplikasi yang aktif
DJANGO_APPS = [
    "unfold",  # Harus sebelum django.contrib.admin
    "unfold.contrib.filters",  # Filter khusus Unfold
    "unfold.contrib.forms",  # Form elements khusus Unfold
    "unfold.contrib.inlines",  # Inline khusus Unfold
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    # Akan diisi saat install library tambahan (Celery, dll)
]

LOCAL_APPS = [
    "apps.vendors",
    "apps.products",
    "apps.monitors",
    "apps.exporters",
    "apps.notifications",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Localization
LANGUAGE_CODE = "id"
TIME_ZONE = "Asia/Jakarta"
USE_I18N = True
USE_TZ = True

# Static & Media
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Django Unfold Admin Theme
UNFOLD = {
    "SITE_TITLE": "Ilyra Marketplace",
    "SITE_HEADER": "Ilyra Marketplace",
    "SITE_SYMBOL": "storefront",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": False,
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": "Navigation",
                "separator": True,
                "items": [
                    {
                        "title": "Dashboard",
                        "icon": "dashboard",
                        "link": "/admin/",
                    },
                ],
            },
            {
                "title": "Toko & Produk",
                "separator": True,
                "items": [
                    {
                        "title": "Toko Vendor",
                        "icon": "store",
                        "link": "/admin/vendors/vendorstore/",
                    },
                    {
                        "title": "Produk",
                        "icon": "inventory_2",
                        "link": "/admin/products/vendorproduct/",
                    },
                ],
            },
        ],
    },
    "COLORS": {
        "primary": {
            "50": "oklch(0.984 0.019 200.873)",
            "100": "oklch(0.956 0.045 203.388)",
            "200": "oklch(0.917 0.08 205.041)",
            "300": "oklch(0.865 0.127 207.078)",
            "400": "oklch(0.789 0.154 211.53)",
            "500": "oklch(0.715 0.143 215.221)", # Warna Cyan Utama
            "600": "oklch(0.609 0.126 221.723)",
            "700": "oklch(0.52 0.105 223.128)",
            "800": "oklch(0.45 0.085 224.283)",
            "900": "oklch(0.398 0.07 227.392)",
            "950": "oklch(0.302 0.056 229.695)",
        },
    },
}