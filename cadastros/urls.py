from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView, name='formulario'),
    path('lista/', views.ListaresponsaveisView, name='lista_responsaveis'),
    path('atualiza/<int:id>',views.AtualizaresponsavelView, name='atualiza_responsavel'),
]