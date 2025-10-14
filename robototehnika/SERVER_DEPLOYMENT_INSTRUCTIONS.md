# Инструкции по развертыванию на сервере

## 🚨 ЭКСТРЕННОЕ РАЗВЕРТЫВАНИЕ ИСПРАВЛЕНИЙ

После force push на сервере возник конфликт веток. Выполните команды в указанном порядке:

### 1. Перейдите в правильную директорию
```bash
cd /home/robotlidab/robototehnika_lida/robototehnika/
```

### 2. Сбросьте локальные изменения и получите новую версию
```bash
git reset --hard origin/master
```

### 3. Проверьте, что код обновился
```bash
git log --oneline -2
```
Должны увидеть коммит: "Fix: Safe Chrome images fix with WhiteNoise fallback"

### 4. Проверьте установку WhiteNoise
```bash
pip list | grep whitenoise
```

### 5. Если WhiteNoise НЕ установлен - установите
```bash
pip install whitenoise==6.9.0
```

### 6. Проверьте конфигурацию Django
```bash
python manage.py check
```
Должно показать: "System check identified no issues"

### 7. Соберите статические файлы
```bash
python manage.py collectstatic --noinput
```

### 8. Перезапустите сервер
```bash
sudo systemctl restart apache2
```

## 🎯 Ожидаемый результат

После выполнения всех команд:
- ✅ Сайт должен заработать
- ✅ Изображения в Chrome должны отображаться корректно
- ✅ WhiteNoise будет работать в продакшене (если установлен)
- ✅ Graceful fallback если WhiteNoise не установлен

## 🔍 Проверка работы

1. Откройте сайт в браузере: https://robotlida.by/
2. Проверьте изображения в Chrome
3. Проверьте консоль разработчика (F12) - не должно быть ошибок 404
4. Проверьте Network вкладку - статические файлы должны загружаться

## 🛡️ Безопасность

- Если WhiteNoise не установлен - сайт работает как раньше
- Если WhiteNoise установлен - получаем улучшения для Chrome
- Никаких критических ошибок не будет благодаря try/except блокам

## 📞 В случае проблем

Если что-то пошло не так:
1. Проверьте логи: `sudo tail -f /var/log/apache2/error.log`
2. Проверьте статус сервера: `sudo systemctl status apache2`
3. Откатитесь к предыдущей версии: `git reset --hard HEAD~1`
