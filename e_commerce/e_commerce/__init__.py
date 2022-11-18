# django_celery/__init__.py

from e_commerce.celery import app as celery_app

__all__ = ("celery_app",)