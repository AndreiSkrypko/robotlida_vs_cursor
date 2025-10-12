"""
Django signals для автоматической отправки уведомлений
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Sign
from .telegram_bot import send_telegram_message, format_new_signup_message
import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Sign)
def notify_new_signup(sender, instance, created, **kwargs):
    """
    Отправляет уведомление в Telegram при создании новой записи на курс
    
    Args:
        sender: Модель Sign
        instance: Созданный объект Sign
        created: True если объект только что создан, False если обновлен
    """
    if created:  # Отправляем уведомление только для новых записей
        try:
            message = format_new_signup_message(instance)
            send_telegram_message(message)
        except Exception as e:
            logger.error(f"Ошибка при отправке уведомления о новой записи: {e}")
            # Не прерываем выполнение, даже если отправка не удалась

