from django.urls import path
from . import views  # importa as views do mesmo app

urlpatterns = [
    path('', views.minha_view, name='minha_view'),
]
