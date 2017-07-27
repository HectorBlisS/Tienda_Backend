from celery import task
from .models import Frase, Today
import random
from celery.task.schedules import crontab
from celery.decorators import periodic_task


@periodic_task(run_every=(crontab()), name="frase", ignore_result=True)
#@task
def change_frase():
    frase = random_frase()
    today = Today.objects.get(id=1)
    while today.frase == frase:
        frase = random_frase()
    today.frase = frase
    today.save()
    print('perro!')


def random_frase():
    frases = Frase.objects.all()
    frase = random.choice(frases)
    return frase