from rest_framework import serializers
# Importa o módulo serializers do Django REST Framework.
# Ele é responsável por transformar modelos (objetos do Django) em JSON
# e também validar dados recebidos em requisições.

from .models import Endereco
# Importa o modelo Endereco que você criou no models.py

class EnderecoSerializer(serializers.ModelSerializer):
    # Criamos uma classe de serializador baseada no ModelSerializer,
    # que já sabe como "traduzir" modelos do Django automaticamente.
    class Meta:
        # Aqui dizemos QUAL modelo será usado e QUAIS campos incluir no JSON.
        model = Endereco # O modelo que vamos converter (Endereco)
        fields = ['id', 'rua', 'bairro', 'cidade', 'estado', 'cep']
        # 'fields' é a lista de campos que vão aparecer na API.
        # 'id' é adicionado automaticamente (chave primária do Django).
