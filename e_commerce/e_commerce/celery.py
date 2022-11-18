# django_celery/celery.py

import os
from celery import Celery
from django.conf import settings



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "e_commerce.settings")
app = Celery("e_commerce")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)






# python -m celery -A e_commerce worker -l info -P gevent  ---1 ci terminalda bu---
# python -m celery -A e_commerce  beat -l info -S django  --- 2 ci terminalda bu---



# python -m celery -A e_commerce worker --beat --scheduler django --loglevel=info -P gevent