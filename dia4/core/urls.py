from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'), #aponta para def em views
    path('consulta_cep/', views.consulta_cep, name = 'consulta_cep')
]
