from django.db import models


class Mensaje(models.Model):
    message = models.CharField(max_length=140)
    perro = models.CharField(max_length=140)

    def __str__(self):
        return self.message



