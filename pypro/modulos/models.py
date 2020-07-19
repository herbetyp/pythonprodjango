from django.db import models


class Modulos(models.Model):
    titulo = models.CharField(max_length=64)
