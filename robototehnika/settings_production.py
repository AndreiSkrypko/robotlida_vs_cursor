"""
Оптимизированные настройки для продакшена
Использование: добавьте эти настройки в конец robototehnika/settings.py

ВНИМАНИЕ: Этот файл ТОЛЬКО для справки! 
Не импортируйте его напрямую!
Скопируйте нужные настройки в основной settings.py
"""
import os
from pathlib import Path

# ВАЖНО: Этот импорт работает только если файл в robototehnika/robototehnika/
# Для использования скопируйте настройки в основной settings.py
# from .settings import *

# === БЕЗОПАСНОСТЬ ===
DEBUG = False
SECRET_KEY = os.getenv('SECRET_KEY', SECRET_KEY)

# === КЕШИРОВАНИЕ ШАБЛОНОВ ===
# Ускоряет рендеринг в 2-3 раза
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'OPTIONS': {
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# === КЕШИРОВАНИЕ (Redis) ===
# Раскомментируйте после установки Redis
# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://127.0.0.1:6379/1',
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#         },
#         'KEY_PREFIX': 'robotlida',
#         'TIMEOUT': 3600,
#     }
# }

# === БАЗА ДАННЫХ (PostgreSQL) ===
# Раскомментируйте после настройки PostgreSQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('DB_NAME', 'robotlida'),
#         'USER': os.getenv('DB_USER', 'robotlida_user'),
#         'PASSWORD': os.getenv('DB_PASSWORD'),
#         'HOST': os.getenv('DB_HOST', 'localhost'),
#         'PORT': os.getenv('DB_PORT', '5432'),
#         'CONN_MAX_AGE': 600,  # Переиспользование соединений
#         'OPTIONS': {
#             'connect_timeout': 10,
#         }
#     }
# }

# === СТАТИЧЕСКИЕ ФАЙЛЫ ===
# Используем WhiteNoise для эффективной раздачи статики
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# === MIDDLEWARE (оптимизированный порядок) ===
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Сжатие и кеш статики
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'main_app.performance_middleware.LazyLoadMiddleware',
]

# === БЕЗОПАСНОСТЬ (продакшен) ===
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 31536000  # 1 год
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# === ЛОГИРОВАНИЕ ===
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'django_errors.log',
            'formatter': 'verbose',
        },
        'telegram_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'telegram_bot.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'main_app.telegram_bot': {
            'handlers': ['telegram_file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

# === СЕССИИ ===
# Используем кеш для сессий (быстрее чем БД)
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# SESSION_CACHE_ALIAS = 'default'

# === ОПТИМИЗАЦИЯ ПРОИЗВОДИТЕЛЬНОСТИ ===
# Уменьшаем количество запросов к БД
SESSION_SAVE_EVERY_REQUEST = False
CONN_MAX_AGE = 600

# === EMAIL (опционально) ===
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
# EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

# === CELERY (для асинхронных задач) ===
# Раскомментируйте после установки Celery
# CELERY_BROKER_URL = 'redis://localhost:6379/0'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'Europe/Minsk'

