from django.db import models


class Frase(models.Model):
    titulo = models.CharField(max_length=140)
    body = models.TextField()
    ref = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo


class Today(models.Model):
    titulo = models.CharField(max_length=140)
    frase = models.ForeignKey(Frase, related_name='today')

    def __str__(self):
        return self.titulo