from rest_framework import viewsets
from . serializers import EnderecoSerializer
from .models import Endereco
import requests

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

    # consumir a api do ViaCep armazenando as informações no banco de dados

    def perform_create(self, serializer):
        cep = serializer.validated_data['cep']
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/', verify=False)

        if response.status_code == 200:
            data = response.json()
            serializer.save(
                cep = cep,
                rua=data.get("logradouro", ""),
                bairro=data.get("bairro", ""),
                cidade=data.get("localidade", ""),
                estado=data.get("uf", ""),
            )
        else:
            return super().perform_create(serializer)
    