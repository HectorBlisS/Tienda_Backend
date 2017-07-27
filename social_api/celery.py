import os
from celery import Celery
from django.conf import settings


#seteamos el default
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'social_api.settings')

app = Celery('social_api', broker="amqp://")

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

