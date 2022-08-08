from calendar import firstweekday
from dataclasses import fields
from datetime import date, datetime
from pyexpat import model
from django.forms import ModelForm
from .models import Entrada, Transacao


class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['valor', 'descricao', 'observacoes', 'categoria']

class EntradaForm(ModelForm):
    class Meta:
        model = Entrada
        fields = ['valor', 'descricao']



#    class Meta:
#        datetime = 'data'
#