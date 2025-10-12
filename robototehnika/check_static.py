#!/usr/bin/env python
"""
Проверка статических файлов Django
Запуск: python check_static.py
"""
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robototehnika.settings')
import django
django.setup()

from django.conf import settings

print("=" * 60)
print("🖼️  ПРОВЕРКА СТАТИЧЕСКИХ ФАЙЛОВ")
print("=" * 60)
print()

print("📁 Настройки статики:")
print(f"   STATIC_URL: {settings.STATIC_URL}")
print(f"   STATIC_ROOT: {settings.STATIC_ROOT}")
print()

# Проверка существования STATIC_ROOT
if os.path.exists(settings.STATIC_ROOT):
    print(f"✅ Директория STATIC_ROOT существует")
    
    # Подсчет файлов
    total_files = 0
    for root, dirs, files in os.walk(settings.STATIC_ROOT):
        total_files += len(files)
    
    print(f"   📊 Найдено файлов: {total_files}")
    
    if total_files == 0:
        print()
        print("⚠️  STATIC_ROOT пустая!")
        print("💡 Выполните: python manage.py collectstatic")
    else:
        # Проверка конкретных директорий
        main_static = os.path.join(settings.STATIC_ROOT, 'main')
        if os.path.exists(main_static):
            print(f"   ✅ main/static найдена")
            
            img_dir = os.path.join(main_static, 'img')
            if os.path.exists(img_dir):
                img_count = sum(len(files) for _, _, files in os.walk(img_dir))
                print(f"   ✅ Картинок найдено: {img_count}")
            else:
                print(f"   ❌ main/img не найдена!")
        else:
            print(f"   ❌ main/static не найдена!")
            print(f"   💡 Выполните: python manage.py collectstatic")
else:
    print(f"❌ Директория STATIC_ROOT не существует!")
    print(f"   Путь: {settings.STATIC_ROOT}")
    print()
    print("💡 Решение:")
    print("   1. python manage.py collectstatic")
    print("   2. Проверьте права доступа к директории")

print()
print("=" * 60)
print("📝 ИНСТРУКЦИЯ ДЛЯ СЕРВЕРА:")
print("=" * 60)
print()
print("Выполните на сервере:")
print("  cd /путь/к/проекту/robototehnika")
print("  python manage.py collectstatic --noinput")
print("  chmod -R 755 static/")
print()
print("Если используете Passenger, также добавьте в .htaccess:")
print('  <IfModule mod_rewrite.c>')
print('    RewriteEngine On')
print('    RewriteRule ^static/(.*)$ static/$1 [L]')
print('  </IfModule>')
print()

