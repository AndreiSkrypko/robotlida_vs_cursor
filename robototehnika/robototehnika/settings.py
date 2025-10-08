from pathlib import Path
import os

# === Базовая директория (там, где manage.py) ===
BASE_DIR = Path(__file__).resolve().parent.parent


# === Безопасность ===
SECRET_KEY = 'django-insecure--^-$0sj_8oonw7-&v@b^(q$m=3v#l%)-tt4h6nz)dcqe3r@z58'
DEBUG = True  # В продакшене — False
ALLOWED_HOSTS = ['robotlida.by', 'www.robotlida.by', 'localhost', '127.0.0.1']

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
    'forum_app',
    'login_app',
]






# === Middleware ===
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# === Тип ID по умолчанию ===
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
