from datetime import datetime
from multiprocessing import context
import django
from django.forms import DateTimeField
from django.shortcuts import get_object_or_404, redirect, render
import datetime
from .models import Entrada, Transacao
from .forms import EntradaForm, TransacaoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']
    data['entrada'] = ['t1']

    data['now'] = datetime.datetime.now()
    return render(request, 'contas/home.html', data)
@login_required
def listagem(request):
    transacoes = Transacao.objects.all()
    entradas = Entrada.objects.all()
    context = {'entradas': entradas, 'transacoes': transacoes}
    return render(request, 'contas/listagem.html', context)
@login_required
def entrada(request):
    entrada = EntradaForm(request.POST or None)
    context = {'entrada': entrada} 
    if entrada.is_valid():
        entrada.save()
        return redirect('url_listagem')

    return render(request, 'contas/entrada.html', context)


@login_required
def nova_transacao(request):
    form = TransacaoForm(request.POST or None)
    data = {}
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form

    return render(request, 'contas/form.html', data)
    #data = {}
    #data['form'] = form
    # ^^ isso é a mesma coisa quê:
    # {'form' : form}#
@login_required
def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    data['transacao'] = transacao 
    return render(request, 'contas/form.html', data)

@login_required
def updatee(request, id_pke):
    entrada = Entrada.objects.get(pk=id_pke)
    entrada = EntradaForm(request.POST or None, instance=entrada)
    if entrada.is_valid():
        entrada.save()
        return redirect('url_listagem')

    context = {'entrada':entrada}

    return render(request, 'contas/entrada.html', context)
    
@login_required
def deletar(request, id_pk):
    id_pk = Transacao.objects.get(pk=id_pk)
    id_pk.delete()

    messages.info(request,"Transação deletada com sucesso.")

    return redirect('url_listagem')
@login_required
def deletare(request, id_pke):
    id_pke = Entrada.objects.get(pk=id_pke)
    id_pke.delete()

    return redirect('url_listagem')


@login_required
def css(pk):
    return(None)