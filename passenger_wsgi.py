import sys
import os

# Путь до проекта
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

# Добавить пути к Python-путям
sys.path.append(PROJECT_PATH)
sys.path.append(os.path.join(PROJECT_PATH, 'robototehnika'))

# Настройки Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'robototehnika.settings'

# Приложение
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
