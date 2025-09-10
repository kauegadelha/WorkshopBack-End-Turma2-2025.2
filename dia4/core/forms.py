#from django.forms import forms
from django import forms
from .models import Endereco

# Criando um formulário baseado no modelo Endereco
class EnderecoForm(forms.ModelForm):
    # Meta: Classe interna de configuração do formulário
    # Define o modelo associado, os campos que aparecem e os rótulos
    class Meta:
        model = Endereco  # Conecta o formulário ao modelo Endereco
        fields = ['cep']  # Só vai usar o campo 'cep' do modelo
        labels = {
            'cep': 'CEP'  # Personaliza o rótulo que aparece no template
        }
# Explicação:
# - forms.ModelForm cria um formulário baseado em um modelo Django.
# - Isso evita precisar definir manualmente cada campo.
# - fields = ['cep'] indica que o formulário só vai exibir/usar o campo 'cep'.
# - labels altera o rótulo que aparece no template, de 'cep' para 'CEP'.
# - Esse formulário permite que o CEP digitado pelo usuário seja validado e salvo diretamente no banco.