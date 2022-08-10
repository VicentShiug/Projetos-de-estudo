import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from list.forms import ListaForm
from .models import Lista
import datetime

@login_required
def lista(request):

    search = request.GET.get('titulo')
    filter = request.GET.get('filter')

    if search:

        listas = Lista.objects.filter(titulo__icontains=search, user=request.user)
    
    elif filter:

        listas = Lista.objects.filter(status=filter, user=request.user)
        
    else:
        listas_pg = Lista.objects.all().order_by('-created_at').filter(user=request.user)
        paginacao = Paginator(listas_pg, 5)

        page = request.GET.get('page')

        listas = paginacao.get_page(page) 

        # def get_queryset(self):
            # titulo = self.objects.filter('12')


            # return Lista.objects.filter(titulo__icontais= titulo)

    return render(request, 'list/lista.html', {'listas' : listas})
@login_required
def listaview(request, id):
    lista = get_object_or_404(Lista, pk=id )
    return render(request, 'list/list.html', {'lista' : lista })

@login_required
def adicionar(request):
    form = ListaForm(request.POST or None)
    if form.is_valid():
        lista = form.save(commit=False)
        lista.user = request.user
        lista.status = 'A Assistir'
        lista.save()

        return redirect('lista')
    return render(request, 'list/adicionar.html', {'form' : form})

@login_required
def editar(request, id):
    lista = Lista.objects.get(pk=id)
    form = ListaForm(request.POST or None, instance=lista)

    if form.is_valid():
        form.save()
        return redirect('lista')

    return render(request, 'list/adicionar.html', {'form' : form, 'lista' : lista})

@login_required 
def delete(request, id):
    lista = Lista.objects.get(pk=id)
    lista.delete()
    return redirect('lista')

# @login_required 
# def user(request):
#     listassss = get_object_or_404(Lista)
#     return render(request, 'list/user.html', {'listassss' : listassss })

@login_required 
def changestatus(request, id):
    lista = get_object_or_404(Lista, pk=id)

    if(lista.status == 'A Assistir'):
        lista.status = 'Assistindo'

    elif(lista.status == 'Assistindo'):
        lista.status = 'Assistido'

    else:
        lista.status = 'A Assistir'

    lista.save()

    return redirect('/')





def user(request):
   
    search = request.GET.get('titulo')
    filter = request.GET.get('filter')
    assistidorecent = Lista.objects.filter(status = 'Assistido', updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30), user=request.user).count()
    listassistindo = Lista.objects.filter(status  = 'Assistindo', user=request.user).count()
    listassistido = Lista.objects.filter(status = 'Assistido' ,user=request.user).count()
    listaassistir = Lista.objects.filter(status = 'A Assistir' ,user=request.user).count()

    if search:
        listas = Lista.objects.filter(titulo__icontains=search, user=request.user)


        listas = Lista.objects.filter(titulo__icontains=search, user=request.user)
    
    elif filter:

        listas = Lista.objects.filter(status=filter, user=request.user)
        
    else:
        listas_pg = Lista.objects.all().order_by('-created_at').filter(user=request.user)
        paginacao = Paginator(listas_pg, 5)

        page = request.GET.get('page')

        listas = paginacao.get_page(page) 

        # def get_queryset(self):
            # titulo = self.objects.filter('12')


            # return Lista.objects.filter(titulo__icontais= titulo)

    return render(request, 'list/user.html', {'listas' : listas, 'assistidorecent': assistidorecent,
                                              'listassistindo': listassistindo,
                                              'listassistido':listassistido,
                                              'listaassistir':listaassistir})
