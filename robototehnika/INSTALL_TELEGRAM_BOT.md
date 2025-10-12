# 🚀 Установка Telegram бота - Пошаговая инструкция

## ✅ Что уже сделано

Telegram бот полностью интегрирован в проект! Созданы все необходимые файлы:

### Файлы системы:
- ✅ `main_app/telegram_bot.py` - утилиты для Telegram
- ✅ `main_app/signals.py` - автоматическая отправка уведомлений
- ✅ `main_app/apps.py` - регистрация signals
- ✅ `robototehnika/settings.py` - настройки (обновлен)
- ✅ `requirements.txt` - добавлен requests

### Документация:
- ✅ `TELEGRAM_QUICKSTART.md` - быстрая настройка
- ✅ `TELEGRAM_BOT_SETUP.md` - подробная инструкция
- ✅ `TELEGRAM_BOT_README.md` - полный обзор
- ✅ `INSTALL_TELEGRAM_BOT.md` - этот файл

### Утилиты:
- ✅ `test_telegram_bot.py` - тестовый скрипт
- ✅ `env.template` - шаблон для .env файла

---

## 📋 Что нужно сделать (5 минут)

### Шаг 1: Создайте Telegram бота

1. Откройте Telegram на телефоне или компьютере
2. Найдите бота **@BotFather**
3. Отправьте команду: `/newbot`
4. Введите название бота, например: `IT Клуб Юные Инженеры`
5. Введите username бота, например: `robotlida_notify_bot`
6. **Скопируйте токен**, который выдаст @BotFather
   - Выглядит так: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`

### Шаг 2: Получите свой Chat ID

**Вариант А (простой):**
1. Найдите в Telegram бота **@userinfobot**
2. Нажмите Start или отправьте любое сообщение
3. Бот пришлёт ваш **Id** - это и есть chat_id
4. **Скопируйте это число** (например: `123456789`)

**Вариант Б (через API):**
1. Найдите вашего созданного бота и нажмите Start
2. Откройте в браузере: `https://api.telegram.org/bot<ВАШ_ТОКЕН>/getUpdates`
3. Найдите значение `"id"` внутри `"chat"` - это ваш chat_id

### Шаг 3: Настройте проект

**Откройте файл:** `robototehnika/robototehnika/settings.py`

**Найдите в конце файла:**
```python
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', 'YOUR_CHAT_ID_HERE')
```

**Замените на:**
```python
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '1234567890:ABCdefGHI...')  # ← Ваш токен
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '123456789')  # ← Ваш chat_id
```

### Шаг 4: Установите зависимости

Откройте командную строку в папке проекта и выполните:

```bash
cd robototehnika
pip install requests==2.32.3
```

Или установите все зависимости:
```bash
pip install -r requirements.txt
```

### Шаг 5: Протестируйте бота

```bash
python test_telegram_bot.py
```

Если всё настроено правильно, вы увидите:
```
✅ Bot Token: 1234567890:ABCdef...
✅ Chat ID: 123456789
📤 Отправка тестового сообщения...
✅ Сообщение успешно отправлено!
```

И **получите сообщение в Telegram**! 🎉

---

## 🎯 Готово! Как это работает?

Теперь при каждой новой записи на курс через сайт:

1. Пользователь заполняет форму записи
2. Django сохраняет данные в базу
3. **Автоматически** отправляется уведомление в Telegram
4. На номер **+375291210908** приходит сообщение:

```
🎓 Новая запись на курс!

👤 Имя: Иван Иванов
📱 Телефон: +375291234567
📚 Курс: детям 7-9 лет
💬 Комментарий: Интересует робототехника

🕐 Время: 12.10.2025 14:30
```

---

## 🔐 Безопасность (Опционально, но рекомендуется)

Чтобы не хранить токен прямо в коде:

### Создайте .env файл:

```bash
cd robototehnika
# Скопируйте шаблон
copy env.template .env
# Или создайте вручную
notepad .env
```

### Добавьте в .env:
```
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
TELEGRAM_CHAT_ID=123456789
```

### Верните в settings.py:
```python
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', 'YOUR_CHAT_ID_HERE')
```

Файл `.env` уже в `.gitignore` и не попадёт в Git! ✅

---

## 🧪 Проверка работы

### 1. Запустите сервер
```bash
python manage.py runserver
```

### 2. Откройте сайт
```
http://127.0.0.1:8000/
```

### 3. Заполните форму записи на курс

### 4. Проверьте Telegram
Должно прийти уведомление! 📱

---

## ❓ Если что-то не работает

### Сообщения не приходят?
```bash
# Проверьте тест
python test_telegram_bot.py

# Проверьте настройки
python manage.py shell
>>> from django.conf import settings
>>> print(settings.TELEGRAM_BOT_TOKEN)
>>> print(settings.TELEGRAM_CHAT_ID)
```

### Ошибка "401 Unauthorized"
- Неправильный токен бота
- Проверьте `TELEGRAM_BOT_TOKEN` в settings.py

### Ошибка "400 Bad Request"
- Неправильный chat_id
- Проверьте, что вы нажали **Start** у бота
- Проверьте `TELEGRAM_CHAT_ID` в settings.py

### Ошибка "Module not found: requests"
```bash
pip install requests==2.32.3
```

---

## 📚 Дополнительная документация

- 📖 **Подробная инструкция:** `TELEGRAM_BOT_SETUP.md`
- ⚡ **Быстрый старт:** `TELEGRAM_QUICKSTART.md`
- 🔍 **Полный обзор:** `TELEGRAM_BOT_README.md`
- 🧪 **Тест бота:** `test_telegram_bot.py`

---

## ✅ Чек-лист

- [ ] Создан бот через @BotFather
- [ ] Получен токен бота
- [ ] Получен chat_id через @userinfobot
- [ ] Токен и chat_id добавлены в settings.py (или .env)
- [ ] Установлен requests: `pip install requests`
- [ ] Запущен тест: `python test_telegram_bot.py`
- [ ] Получено тестовое сообщение в Telegram
- [ ] Проверена работа при реальной записи на курс

---

## 🎉 Поздравляем!

Telegram бот настроен и готов к работе!

Теперь вы будете **автоматически получать уведомления** о каждой новой записи на курсы.

**Номер для уведомлений:** +375291210908

---

**Время настройки:** ~5 минут  
**Версия:** 1.0  
**Дата:** 12.10.2025  
**Статус:** ✅ Готово к использованию

