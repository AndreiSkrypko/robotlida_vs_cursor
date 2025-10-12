#!/usr/bin/env python
"""
Диагностика настроек Telegram бота
Запуск: python check_telegram_config.py
"""
import os
import sys

print("=" * 60)
print("🔍 ДИАГНОСТИКА TELEGRAM БОТА")
print("=" * 60)
print()

# Проверка 1: Django settings
print("1️⃣ Проверка Django настроек...")
try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robototehnika.settings')
    import django
    django.setup()
    from django.conf import settings
    
    bot_token = getattr(settings, 'TELEGRAM_BOT_TOKEN', None)
    chat_id = getattr(settings, 'TELEGRAM_CHAT_ID', None)
    
    if not bot_token:
        print("   ❌ TELEGRAM_BOT_TOKEN не найден в settings.py")
        sys.exit(1)
    elif bot_token == 'YOUR_BOT_TOKEN_HERE':
        print("   ❌ TELEGRAM_BOT_TOKEN не настроен (значение по умолчанию)")
        print("   💡 Создайте файл .env со строкой:")
        print("      TELEGRAM_BOT_TOKEN=8361655264:AAGCs-IKDC_zPJn5Nyj0yg62tswU9wrJSHo")
        sys.exit(1)
    else:
        print(f"   ✅ Bot Token найден: {bot_token[:20]}...")
    
    if not chat_id:
        print("   ❌ TELEGRAM_CHAT_ID не найден в settings.py")
        sys.exit(1)
    elif chat_id == 'YOUR_CHAT_ID_HERE':
        print("   ❌ TELEGRAM_CHAT_ID не настроен (значение по умолчанию)")
        print("   💡 Создайте файл .env со строкой:")
        print("      TELEGRAM_CHAT_ID=1053151551")
        sys.exit(1)
    else:
        print(f"   ✅ Chat ID найден: {chat_id}")
    
except Exception as e:
    print(f"   ❌ Ошибка при загрузке Django: {e}")
    sys.exit(1)

print()

# Проверка 2: Библиотека requests
print("2️⃣ Проверка библиотеки requests...")
try:
    import requests
    print(f"   ✅ requests установлен (версия {requests.__version__})")
except ImportError:
    print("   ❌ requests не установлен")
    print("   💡 Установите: pip install requests")
    sys.exit(1)

print()

# Проверка 3: Файл .env
print("3️⃣ Проверка файла .env...")
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
if os.path.exists(env_path):
    print(f"   ✅ Файл .env найден: {env_path}")
    with open(env_path, 'r') as f:
        content = f.read()
        if 'TELEGRAM_BOT_TOKEN' in content:
            print("   ✅ TELEGRAM_BOT_TOKEN найден в .env")
        else:
            print("   ⚠️  TELEGRAM_BOT_TOKEN не найден в .env")
        if 'TELEGRAM_CHAT_ID' in content:
            print("   ✅ TELEGRAM_CHAT_ID найден в .env")
        else:
            print("   ⚠️  TELEGRAM_CHAT_ID не найден в .env")
else:
    print("   ⚠️  Файл .env не найден")
    print("   💡 Создайте файл .env с содержимым:")
    print("      TELEGRAM_BOT_TOKEN=8361655264:AAGCs-IKDC_zPJn5Nyj0yg62tswU9wrJSHo")
    print("      TELEGRAM_CHAT_ID=1053151551")

print()

# Проверка 4: Подключение к Telegram API
print("4️⃣ Проверка подключения к Telegram API...")
try:
    url = f"https://api.telegram.org/bot{bot_token}/getMe"
    response = requests.get(url, timeout=10)
    
    if response.status_code == 200:
        data = response.json()
        if data.get('ok'):
            bot_info = data.get('result', {})
            print(f"   ✅ Соединение с Telegram API успешно")
            print(f"   ✅ Бот: @{bot_info.get('username', 'unknown')}")
        else:
            print(f"   ❌ Ошибка API: {data}")
    elif response.status_code == 401:
        print("   ❌ Неверный токен бота (401 Unauthorized)")
        print("   💡 Проверьте правильность токена")
    else:
        print(f"   ❌ Ошибка {response.status_code}: {response.text}")
        
except requests.exceptions.Timeout:
    print("   ❌ Таймаут подключения к Telegram")
    print("   💡 Проверьте интернет-соединение на сервере")
except requests.exceptions.RequestException as e:
    print(f"   ❌ Ошибка подключения: {e}")
    print("   💡 Проверьте интернет-соединение и firewall")
except Exception as e:
    print(f"   ❌ Неожиданная ошибка: {e}")

print()

# Проверка 5: Отправка тестового сообщения
print("5️⃣ Отправка тестового сообщения...")
try:
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': '🧪 Тест с сервера: бот работает!',
        'parse_mode': 'HTML'
    }
    
    response = requests.post(url, data=payload, timeout=10)
    
    if response.status_code == 200:
        data = response.json()
        if data.get('ok'):
            print("   ✅ Сообщение успешно отправлено!")
            print("   📱 Проверьте Telegram")
        else:
            print(f"   ❌ Ошибка API: {data}")
    elif response.status_code == 400:
        print("   ❌ Ошибка 400: Bad Request")
        print("   💡 Возможные причины:")
        print("      - Неправильный chat_id")
        print("      - Вы не нажали Start у бота")
        print("   💡 Решение: откройте @robotlida_notify_bot и нажмите Start")
    elif response.status_code == 401:
        print("   ❌ Ошибка 401: Unauthorized")
        print("   💡 Неверный токен бота")
    else:
        print(f"   ❌ Ошибка {response.status_code}")
        print(f"   Ответ: {response.text}")
        
except Exception as e:
    print(f"   ❌ Ошибка: {e}")

print()
print("=" * 60)
print("✅ Диагностика завершена")
print("=" * 60)

