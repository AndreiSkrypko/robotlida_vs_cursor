"""
Утилита для отправки уведомлений в Telegram
"""
import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


def send_telegram_message(message):
    """
    Отправляет сообщение в Telegram через Bot API
    
    Args:
        message (str): Текст сообщения для отправки
        
    Returns:
        bool: True если сообщение отправлено успешно, False в противном случае
    """
    # Получаем настройки из settings.py
    bot_token = getattr(settings, 'TELEGRAM_BOT_TOKEN', None)
    chat_id = getattr(settings, 'TELEGRAM_CHAT_ID', None)
    
    if not bot_token or not chat_id:
        logger.error("Telegram bot token или chat_id не настроены в settings.py")
        return False
    
    # URL для Telegram Bot API
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    # Параметры запроса
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML'  # Поддержка HTML форматирования
    }
    
    try:
        response = requests.post(url, data=payload, timeout=10)
        response.raise_for_status()
        
        if response.json().get('ok'):
            logger.info(f"Telegram сообщение успешно отправлено в chat_id: {chat_id}")
            return True
        else:
            logger.error(f"Ошибка отправки в Telegram: {response.json()}")
            return False
            
    except requests.exceptions.RequestException as e:
        logger.error(f"Исключение при отправке в Telegram: {e}")
        return False
    except Exception as e:
        logger.error(f"Неожиданная ошибка при отправке в Telegram: {e}")
        return False


def format_new_signup_message(signup):
    """
    Форматирует сообщение о новой записи на курс
    
    Args:
        signup: Объект модели Sign
        
    Returns:
        str: Отформатированное сообщение
    """
    message = f"""
🎓 <b>Новая запись на курс!</b>

👤 <b>Имя:</b> {signup.name}
📱 <b>Телефон:</b> {signup.phone}
📚 <b>Курс:</b> {signup.course.name}
"""
    
    if signup.comment:
        message += f"💬 <b>Комментарий:</b> {signup.comment}\n"
    
    # Форматируем дату и время
    created_time = signup.created_at.strftime('%d.%m.%Y %H:%M')
    message += f"\n🕐 <b>Время:</b> {created_time}"
    
    return message

