from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Endereco
from .serializers import EnderecoSerializer
import requests

# 📌 Listar e Criar Endereços
@api_view(['GET', 'POST'])
def endereco_list_create(request):
    if request.method == 'GET':
        enderecos = Endereco.objects.all()
        serializer = EnderecoSerializer(enderecos, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = EnderecoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 📌 Detalhar, Atualizar e Deletar Endereço por ID
@api_view(['GET', 'PUT', 'DELETE'])
def endereco_detail(request, pk):
    try:
        endereco = Endereco.objects.get(pk=pk)
    except Endereco.DoesNotExist:
        return Response({'error': 'Endereço não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EnderecoSerializer(endereco)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = EnderecoSerializer(endereco, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        endereco.delete()
        return Response({'message': 'Endereço deletado com sucesso'}, status=status.HTTP_204_NO_CONTENT)

# 📌 Criar Endereço automaticamente usando a API pública ViaCEP
@api_view(['POST'])
def endereco_via_cep(request):
    cep = request.data.get('cep')

    if not cep:
        return Response({'error': 'CEP é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/', timeout=5)
        data = response.json()

        if 'erro' in data:
            return Response({'error': 'CEP inválido'}, status=status.HTTP_400_BAD_REQUEST)

        endereco_data = {
            'rua': data.get('logradouro', ''),
            'bairro': data.get('bairro', ''),
            'cidade': data.get('localidade', ''),
            'estado': data.get('uf', ''),
            'cep': data.get('cep', '')
        }

        serializer = EnderecoSerializer(data=endereco_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


