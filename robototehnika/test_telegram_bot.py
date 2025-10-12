#!/usr/bin/env python
"""
Тестовый скрипт для проверки работы Telegram бота
Запуск: python test_telegram_bot.py
"""
import os
import django

# Настройка Django окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robototehnika.settings')
django.setup()

from main_app.telegram_bot import send_telegram_message
from django.conf import settings


def test_bot():
    """Тестирует отправку сообщения через Telegram бота"""
    print("🤖 Тест Telegram бота")
    print("=" * 50)
    
    # Проверка настроек
    bot_token = getattr(settings, 'TELEGRAM_BOT_TOKEN', None)
    chat_id = getattr(settings, 'TELEGRAM_CHAT_ID', None)
    
    if not bot_token or bot_token == 'YOUR_BOT_TOKEN_HERE':
        print("❌ ОШИБКА: TELEGRAM_BOT_TOKEN не настроен в settings.py")
        print("   Откройте robototehnika/settings.py и укажите токен бота")
        return False
    
    if not chat_id or chat_id == 'YOUR_CHAT_ID_HERE':
        print("❌ ОШИБКА: TELEGRAM_CHAT_ID не настроен в settings.py")
        print("   Откройте robototehnika/settings.py и укажите chat_id")
        return False
    
    print(f"✅ Bot Token: {bot_token[:20]}...")
    print(f"✅ Chat ID: {chat_id}")
    print()
    
    # Отправка тестового сообщения
    test_message = """
🧪 <b>Тестовое сообщение</b>

Это тестовое сообщение для проверки работы Telegram бота.

✅ Если вы видите это сообщение, бот работает правильно!

🎓 IT Клуб Юные Инженеры
🌐 robotlida.by
"""
    
    print("📤 Отправка тестового сообщения...")
    success = send_telegram_message(test_message)
    
    if success:
        print("✅ Сообщение успешно отправлено!")
        print("   Проверьте Telegram - должно прийти уведомление")
        return True
    else:
        print("❌ Ошибка при отправке сообщения")
        print("   Проверьте:")
        print("   1. Правильность токена и chat_id")
        print("   2. Нажали ли вы Start у бота")
        print("   3. Есть ли интернет соединение")
        return False


if __name__ == '__main__':
    test_bot()

