# Importa a função path, usada para definir URLs no Django
from django.urls import path
# Importa as views do app atual, que são as funções que processam as requisições
from . import views

# Lista de URLs do app
urlpatterns = [
    # URL raiz do app ('/'), chama a view 'home' definida em views.py
    # 'name' serve como identificador da URL para usar em templates ou redirecionamentos
    path('', views.home, name ='home'),

    # URL '/consulta_cep/', chama a view 'consulta_cep' definida em views.py
    # 'name' = 'consulta_cep' permite referenciar essa URL de forma fácil no projeto
    path('consulta_cep/', views.consulta_cep, name = 'consulta_cep')
]
