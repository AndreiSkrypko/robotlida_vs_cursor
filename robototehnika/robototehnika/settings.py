from pathlib import Path
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла (если он есть)
load_dotenv()

# === Базовая директория (там, где manage.py) ===
BASE_DIR = Path(__file__).resolve().parent.parent


# === Безопасность ===
SECRET_KEY = 'django-insecure--^-$0sj_8oonw7-&v@b^(q$m=3v#l%)-tt4h6nz)dcqe3r@z58'
# DEBUG читается из .env, по умолчанию False (безопасно для продакшена)
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['robotlida.by', 'www.robotlida.by', 'localhost', '127.0.0.1', 'testserver']

# === Приложения ===
INSTALLED_APPS = [
    'widget_tweaks',
    'main_app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',  # для динамического sitemap.xml
    'django.contrib.sites',  # для Django sitemaps
    'forum_app',
    'login_app',
]






# === Middleware ===
MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'main_app.performance_middleware.LazyLoadMiddleware',
]

# === URLs и WSGI ===
ROOT_URLCONF = 'robototehnika.urls'
WSGI_APPLICATION = 'robototehnika.wsgi.application'

# === Шаблоны ===
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # можно создать папку templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# === База данных ===
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# === Валидация паролей ===
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# === Локализация ===
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Minsk'
USE_I18N = True
USE_TZ = True

# === Статика и медиа ===
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Настройки для статических файлов в продакшене
STATICFILES_DIRS = [
    BASE_DIR / 'main_app' / 'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# === БЕЗОПАСНОЕ ДОБАВЛЕНИЕ WHITENOISE ===
try:
    import whitenoise
    # WhiteNoise доступен - добавляем настройки для продакшена
    if not DEBUG:
        STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
        
        # Добавляем WhiteNoise middleware в начало списка (после SecurityMiddleware)
        if 'whitenoise.middleware.WhiteNoiseMiddleware' not in MIDDLEWARE:
            # Находим позицию SecurityMiddleware и добавляем WhiteNoise после него
            security_index = MIDDLEWARE.index('django.middleware.security.SecurityMiddleware')
            MIDDLEWARE.insert(security_index + 1, 'whitenoise.middleware.WhiteNoiseMiddleware')
            
        print("WhiteNoise настроен для продакшена")
except ImportError:
    print("WhiteNoise не установлен - используем стандартную раздачу статики")
    pass

# === Тип ID по умолчанию ===
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# === Для Django Sites Framework ===
SITE_ID = 1

# === Настройки для продакшена и SEO ===
# Безопасность (раскомментировать в продакшене)
# SECURE_SSL_REDIRECT = True  # Перенаправление на HTTPS
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# X_FRAME_OPTIONS = 'DENY'

# === Настройки Telegram Bot ===
# ВАЖНО: Замените эти значения на свои!
# Как получить токен: @BotFather в Telegram -> /newbot
# Как получить chat_id: напишите боту @userinfobot и скопируйте Id
# 
# Для безопасности можно использовать переменные окружения (.env файл):
# TELEGRAM_BOT_TOKEN=ваш_токен
# TELEGRAM_CHAT_ID=ваш_chat_id
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', 'YOUR_CHAT_ID_HERE')