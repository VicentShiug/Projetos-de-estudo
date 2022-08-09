from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.lista, name="lista"),
    path('list/<int:id>', views.listaview, name='lista-view'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('user/', views.user, name='user'),
    path('changestatus/<int:id>', views.changestatus, name='changestatus'),


]
