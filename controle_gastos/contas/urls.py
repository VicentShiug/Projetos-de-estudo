from xml.etree.ElementInclude import include
import django
from django.urls import path, include
from . import views




urlpatterns = [
    path('', views.listagem, name='url_listagem'),
    path('home/', views.home),
    path('form/',views.nova_transacao, name= 'url_form'),
    path('update/<int:pk>/', views.update, name='url_update'),
    path('updatee/<int:id_pke>/', views.updatee, name='url_updatee'),
    path('deletar/<int:id_pk>', views.deletar, name='url_deletar'),
    path('deletare/<int:id_pke>', views.deletare, name='url_deletare'),
    path('home/css', views.css),
    path('entrada/',views.entrada, name='url_entrada'),

]
