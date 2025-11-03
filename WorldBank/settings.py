"""
Django settings for WorldBank project.
"""

import os
from pathlib import Path
from decouple import config

# BASE DIRECTORY
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = config("DJANGO_SECRET_KEY", default="your-default-secret-key")
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = [
    "worldbank-backend.onrender.com",  # Render backend domain
    "127.0.0.1",
    "localhost",
    config("ALLOWED_HOST", default=""),  # Optional extra host
]

# INSTALLED APPS
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "feedback",  # your app
    "rest_framework",
    "corsheaders",
]

# MIDDLEWARE (CORS must come before CommonMiddleware)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # must come before CommonMiddleware
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "WorldBank.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "WorldBank.wsgi.application"

# DATABASE CONFIGURATION (MySQL on cPanel phpMyAdmin)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),  # Example: "newhorizonsnigeria.net.ng"
        "PORT": config("DB_PORT", default="3306"),
        "OPTIONS": {"init_command": "SET sql_mode='STRICT_TRANS_TABLES'"},
    }
}

# PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# INTERNATIONALIZATION
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# STATIC & MEDIA FILES
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# DEFAULT PRIMARY KEY FIELD TYPE
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ✅ CORS SETTINGS
CORS_ALLOWED_ORIGINS = [
    "https://worldbank-feedbank.vercel.app",  # Production frontend on Vercel
    "http://localhost:3000",  # Local development
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
CORS_ALLOW_HEADERS = ["content-type", "authorization"]

# ✅ SECURITY SETTINGS
CSRF_TRUSTED_ORIGINS = [
    "https://worldbank-feedbank.vercel.app",
    "https://worldbank-backend.onrender.com",
]

# ✅ Optional: allow all origins temporarily (for testing only)
# CORS_ALLOW_ALL_ORIGINS = True
