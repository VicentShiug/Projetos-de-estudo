from secrets import choice
from sre_constants import AT_UNI_BOUNDARY
from telnetlib import STATUS
from venv import create
from django.db import models
from django.contrib.auth import get_user_model


class Lista(models.Model):
    STATUS = (
    ('Assistindo','Assistindo'),
    ('Assistido', 'Assistido'),
    ('A Assistir','A Assistir'),
    )
    Tipo = (
        ('Filme', 'Filme'),
        ('Anime','Anime'),
        ('Série','Série'),

    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=STATUS,
        blank=True,
        
    )
    tipo = models.CharField(
        max_length=5,
        choices=Tipo
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

  
    def __str__(self):
        return self.titulo

