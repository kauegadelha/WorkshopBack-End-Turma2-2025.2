from rest_framework import viewsets
# Importa os viewsets do DRF.
# ViewSets já vêm com funcionalidades de CRUD (Create, Read, Update, Delete) prontas.

from . serializers import EnderecoSerializer
# Importa o serializer que é o "tradutor" dos dados do modelo Endereco

from .models import Endereco
import requests

class EnderecoViewSet(viewsets.ModelViewSet):
    # ModelViewSet é um tipo de ViewSet que já possui
    # todas as operações básicas de CRUD implementadas automaticamente.

    queryset = Endereco.objects.all()
    # Define que todos os endereços do banco serão o "conjunto de dados" padrão
    # para essa ViewSet

    serializer_class = EnderecoSerializer
    # Define que essa ViewSet vai usar o EnderecoSerializer
    # para traduzir os dados entre JSON e banco

    # consumir a api do ViaCep armazenando as informações no banco de dados

    def perform_create(self, serializer):
        # Esse método é chamado quando alguém cria um novo endereço via API (POST)

        cep = serializer.validated_data['cep']
        # Pega o CEP enviado pelo usuário e já validado pelo serializer

        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/', verify=False)
        # Faz uma requisição para a API do ViaCep para obter os dados do endereço
        # verify=False → ignora certificado SSL (não recomendado em produção)

        if response.status_code == 200: # Se a requisição deu certo (HTTP 200)
            data = response.json()
            # Converte a resposta da API para JSON (um dicionário Python)
            serializer.save(
                cep = cep,
                rua=data.get("logradouro", ""), # pega o logradouro ou deixa vazio se não existir
                bairro=data.get("bairro", ""),  # pega o bairro ou deixa vazio se não existir
                cidade=data.get("localidade", ""), # pega a cidade
                estado=data.get("uf", ""), # pega o estado (UF)
            )
        else:
            # Se a requisição não deu certo, salva apenas com os dados enviados
            return super().perform_create(serializer)
    