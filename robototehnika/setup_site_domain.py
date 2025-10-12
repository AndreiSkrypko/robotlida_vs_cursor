#!/usr/bin/env python
"""
Скрипт для настройки правильного домена сайта для sitemap.xml
Запуск: python setup_site_domain.py
"""

import os
import django

# Настройка Django окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robototehnika.settings')
django.setup()

from django.contrib.sites.models import Site

def setup_domain():
    """Настраивает правильный домен для сайта"""
    try:
        site = Site.objects.get(id=1)
        site.domain = 'robotlida.by'
        site.name = 'Робот Лида - Робототехника для детей'
        site.save()
        print(f"✓ Домен успешно обновлен: {site.domain}")
        print(f"✓ Название сайта: {site.name}")
        return True
    except Site.DoesNotExist:
        print("✗ Ошибка: Site с ID=1 не найден")
        print("  Создаем новый сайт...")
        site = Site.objects.create(
            id=1,
            domain='robotlida.by',
            name='Робот Лида - Робототехника для детей'
        )
        print(f"✓ Сайт создан: {site.domain}")
        return True
    except Exception as e:
        print(f"✗ Ошибка: {e}")
        return False

if __name__ == '__main__':
    print("="*60)
    print("НАСТРОЙКА ДОМЕНА САЙТА")
    print("="*60)
    success = setup_domain()
    print("="*60)
    if success:
        print("\n✓ Настройка завершена! Теперь sitemap.xml будет использовать")
        print("  правильный домен robotlida.by")
    else:
        print("\n✗ Произошла ошибка при настройке")

