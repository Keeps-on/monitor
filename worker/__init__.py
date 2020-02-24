import os
# import djcelery

from celery import Celery, platforms

platforms.C_FORCE_ROOT = True  # 加上这一行
from worker import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monitor.settings")

celery_app = Celery('worker')
celery_app.config_from_object(config)
celery_app.autodiscover_tasks()
