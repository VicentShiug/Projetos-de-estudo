from dataclasses import Field
from pyexpat import model
from django.forms import ModelForm

from .models import Lista

class ListaForm(ModelForm):
    class Meta:
        model = Lista
        fields = ['titulo', 'descricao', 'status', 'tipo',]
