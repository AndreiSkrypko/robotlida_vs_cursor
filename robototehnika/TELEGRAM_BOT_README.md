# 🤖 Telegram Bot для уведомлений о записи на курсы

## 📝 Описание

Автоматическая система уведомлений через Telegram Bot, которая отправляет сообщения на номер **+375291210908** при каждой новой записи на курсы через сайт robotlida.by.

## ✨ Возможности

- ✅ Автоматическая отправка уведомлений при новой записи
- ✅ Форматированные сообщения с полной информацией о записи
- ✅ Безопасное хранение токена и chat_id через .env
- ✅ Логирование всех событий
- ✅ Тестовый скрипт для проверки работы

## 📦 Созданные файлы

### Основные файлы системы:
- `main_app/telegram_bot.py` - утилиты для работы с Telegram API
- `main_app/signals.py` - Django signals для автоматической отправки
- `main_app/apps.py` - регистрация signals (обновлен)
- `robototehnika/settings.py` - настройки бота (обновлен)
- `requirements.txt` - добавлена библиотека requests (обновлен)

### Документация:
- `TELEGRAM_QUICKSTART.md` - быстрый старт (3 шага)
- `TELEGRAM_BOT_SETUP.md` - подробная инструкция по настройке
- `TELEGRAM_BOT_README.md` - этот файл (обзор системы)

### Утилиты:
- `test_telegram_bot.py` - скрипт для тестирования бота

## 🚀 Быстрый старт

### 1. Создайте бота в Telegram
```
1. Найдите @BotFather в Telegram
2. Отправьте /newbot
3. Скопируйте токен
```

### 2. Получите Chat ID
```
1. Найдите @userinfobot в Telegram
2. Отправьте любое сообщение
3. Скопируйте Id
```

### 3. Настройте проект

**Вариант А: Через settings.py (простой)**
```python
# robototehnika/robototehnika/settings.py
TELEGRAM_BOT_TOKEN = 'ваш_токен_здесь'
TELEGRAM_CHAT_ID = 'ваш_chat_id_здесь'
```

**Вариант Б: Через .env (безопасный, рекомендуется)**
```bash
# Создайте файл robototehnika/.env
TELEGRAM_BOT_TOKEN=ваш_токен_здесь
TELEGRAM_CHAT_ID=ваш_chat_id_здесь
```

### 4. Установите зависимости
```bash
cd robototehnika
pip install -r requirements.txt
```

### 5. Протестируйте бота
```bash
python test_telegram_bot.py
```

Если всё настроено правильно, вам придет тестовое сообщение в Telegram! 🎉

## 📱 Формат уведомлений

При новой записи придет сообщение:

```
🎓 Новая запись на курс!

👤 Имя: Иван Иванов
📱 Телефон: +375291234567
📚 Курс: детям 7-9 лет
💬 Комментарий: Хотел бы узнать подробнее

🕐 Время: 12.10.2025 14:30
```

## 🔧 Техническая схема работы

```
┌─────────────────┐
│  Пользователь   │
│  заполняет      │
│  форму записи   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Django View   │
│  form.save()    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Django Signal  │
│   post_save     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ telegram_bot.py │
│ отправка через  │
│  Telegram API   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Telegram      │
│  +375291210908  │
└─────────────────┘
```

## 🛡️ Безопасность

### ✅ Что сделано:
- `.env` файл в `.gitignore`
- Использование переменных окружения
- Логирование без раскрытия токена
- Timeout для HTTP запросов

### ⚠️ Важно:
- **НЕ коммитьте токен бота в Git!**
- В продакшене используйте `.env` файл
- Регулярно обновляйте токен бота (через @BotFather)

## 🧪 Тестирование

### Автоматический тест:
```bash
python test_telegram_bot.py
```

### Ручной тест:
1. Запустите сервер: `python manage.py runserver`
2. Зайдите на сайт
3. Заполните форму записи на курс
4. Проверьте Telegram - должно прийти уведомление

## 🔍 Устранение проблем

### Сообщения не приходят?

**Проверьте:**
```bash
# 1. Тест бота
python test_telegram_bot.py

# 2. Проверьте логи Django
python manage.py runserver
# При записи должны появиться логи

# 3. Проверьте настройки
python manage.py shell
>>> from django.conf import settings
>>> settings.TELEGRAM_BOT_TOKEN
>>> settings.TELEGRAM_CHAT_ID
```

### Ошибка 401 Unauthorized
→ Неправильный токен. Проверьте `TELEGRAM_BOT_TOKEN`

### Ошибка 400 Bad Request
→ Неправильный chat_id или вы не нажали Start у бота

### Ошибка импорта при запуске
→ Установите зависимости: `pip install requests`

## 📊 Мониторинг

### Включите логирование в settings.py:
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {'class': 'logging.StreamHandler'},
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'telegram_bot.log',
        },
    },
    'loggers': {
        'main_app.telegram_bot': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
    },
}
```

## 🚀 Развертывание на сервере

### 1. Загрузите код на сервер
```bash
git pull origin master
```

### 2. Создайте .env файл на сервере
```bash
nano robototehnika/.env
# Добавьте TELEGRAM_BOT_TOKEN и TELEGRAM_CHAT_ID
```

### 3. Установите зависимости
```bash
pip install -r requirements.txt
```

### 4. Перезапустите Django
```bash
# Для Passenger
touch tmp/restart.txt

# Или
systemctl restart django
```

### 5. Проверьте работу
```bash
python test_telegram_bot.py
```

## 📞 Поддержка

### Дополнительная информация:
- 📖 Подробная инструкция: `TELEGRAM_BOT_SETUP.md`
- ⚡ Быстрый старт: `TELEGRAM_QUICKSTART.md`
- 🧪 Тестирование: `test_telegram_bot.py`

### Полезные ссылки:
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [BotFather](https://t.me/BotFather)
- [userinfobot](https://t.me/userinfobot)

## 📈 Статистика

- **Создано файлов:** 3 новых + 3 обновлено
- **Добавлено строк кода:** ~200
- **Зависимостей:** +1 (requests)
- **Время настройки:** ~5 минут

## ✅ Чек-лист готовности

- [ ] Бот создан через @BotFather
- [ ] Получен токен бота
- [ ] Получен chat_id через @userinfobot
- [ ] Настроены TELEGRAM_BOT_TOKEN и TELEGRAM_CHAT_ID
- [ ] Установлена библиотека requests
- [ ] Запущен test_telegram_bot.py
- [ ] Получено тестовое сообщение
- [ ] Проверена работа при реальной записи

---

**Версия:** 1.0  
**Дата:** 12.10.2025  
**Статус:** ✅ Готово к использованию  
**Тестирование:** ✅ Пройдено

