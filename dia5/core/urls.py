from django.urls import path
from .views import ViaCepFormView, ViaCepListView, ViaCepDetailView, ViaCepDeleteView, home, consulta_cep


app_name = "viacep"
# Lista de URLs do app
urlpatterns = [
    path('home', home, name ='home'),
    path('consulta_cep/', consulta_cep, name = 'consulta_cep'),
    path('', ViaCepFormView.as_view(), name='create'), 
    path('list/', ViaCepListView.as_view(), name='list'),
    path('detail/<int:pk>/', ViaCepDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', ViaCepDeleteView.as_view(), name='delete'),
]
