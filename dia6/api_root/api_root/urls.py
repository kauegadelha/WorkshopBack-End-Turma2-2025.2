"""
URL configuration for api_root project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin # Importa o painel administrativo do Django
from django.urls import path, include
# 'path' serve para criar URLs
# 'include' permite incluir outros arquivos de URL (modularização)
from rest_framework.routers import DefaultRouter
# Importa o DefaultRouter do DRF
# Ele cria automaticamente as rotas CRUD (GET, POST, PUT, DELETE) para os ViewSets
from api_rest.viewsets import EnderecoViewSet
# Importa a ViewSet que criamos para os endereços

router = DefaultRouter() # Cria um "roteador" que vai mapear as URLs automaticamente
router.register(r'enderecos', EnderecoViewSet)
# Registra a ViewSet no roteador
# Agora sua API terá endpoints como:
# - GET /enderecos/       → lista todos os endereços
# - POST /enderecos/      → cria um novo endereço
# - GET /enderecos/<id>/  → pega detalhes de um endereço específico
# - PUT /enderecos/<id>/  → atualiza um endereço
# - DELETE /enderecos/<id>/ → deleta um endereço

urlpatterns = [
    path('admin/', admin.site.urls), # URL para acessar o painel de administração do Django
    path('', include(router.urls)),
    # Inclui as URLs geradas automaticamente pelo roteador da API
    # Isso é o que cria o endpoint raiz da sua API ("/") e o "/enderecos/"
    path('api-auth/', include('rest_framework.urls')),
    # Adiciona URLs de login/logout do DRF para testar a API na interface web
]
