from django.contrib import admin
from .models import Categoria, Entrada
from .models import Transacao

admin.site.register(Categoria)
admin.site.register(Transacao)
admin.site.register(Entrada)