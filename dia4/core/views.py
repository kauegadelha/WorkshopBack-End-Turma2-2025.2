# Importa a função render, usada para renderizar (exibir) templates HTML
from django.shortcuts import render
# Importa o modelo Endereco, que representa a tabela no banco de dados
from .models import Endereco
# Importa o formulário EnderecoForm, que captura o CEP digitado pelo usuário
from .forms import EnderecoForm
# Importa a biblioteca requests, que permite fazer requisições HTTP para APIs externas
import requests
from requests.exceptions import RequestException

# View responsável por exibir a página inicial (home)
def home(request):
    # Renderiza o template 'home.html', que deve conter o formulário para o usuário digitar o CEP
    return render(request, 'app/home.html') 

# View responsável por processar o CEP digitado, consultar a API e salvar os dados
def consulta_cep(request):
    # Cria o formulário EnderecoForm a partir dos dados da requisição (se existirem)
    form = EnderecoForm(request.GET or None)
    # Verifica se o formulário é válido (se o CEP foi preenchido corretamente)
    if form.is_valid():
        # Pega o valor do campo 'cep' já validado
        cep = form.cleaned_data['cep']
        try:
            # Faz a requisição para a API ViaCEP usando o CEP digitado
            response = requests.get(f'https://viacep.com.br/ws/{cep}/json', timeout=5)
            response.raise_for_status() # Levanta erro se status != 200

            # Verifica se a resposta da API foi bem-sucedida (status 200)
            # mesma coisa do response.raise: if response.status_code == 200:

            # Converte a resposta em JSON (um dicionário Python)
            data = response.json()
            print(data) # Apenas para debug: imprime no console os dados recebidos da API

            # Cria um objeto Endereco com os dados retornados pela API
            endereco = Endereco(
                cep=data.get('cep'),
                rua = data.get('logradouro'),
                bairro = data.get('bairro'),
                cidade = data.get('localidade'),
                estado = data.get('uf'),

            )
            # Salva o objeto endereco no banco de dados
            endereco.save()
            # Renderiza o template 'consulta_cep.html', passando o objeto endereco para exibição
            return render(request, 'consulta_cep.html', {'endereco': endereco})
        except RequestException:
            # Caso a requisição falhe, renderiza o template sem o endereço
            return render(request, 'app/consulta_cep.html', {'endereco': None})
