# celeryy.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Устанавливаем переменную окружения для настроек Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings")

# Создаем экземпляр Celery
app = Celery("drf")

# Загружаем настройки из настроек Django
app.config_from_object("django.conf:settings", namespace="CELERY")

# Автоматически обнаруживаем и регистрируем задачи из файлов tasks.py в приложениях Django
app.autodiscover_tasks()
