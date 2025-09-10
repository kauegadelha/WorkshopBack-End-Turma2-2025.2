#from django.forms import forms
from django import forms
from .models import Endereco

# Criando um formulário baseado no modelo Endereco
class ViaCepForm(forms.ModelForm):
    # Meta: Classe interna de configuração do formulário
    # Define o modelo associado, os campos que aparecem e os rótulos
    class Meta:
        model = Endereco  # Conecta o formulário ao modelo Endereco
        fields = ['cep']  # Só vai usar o campo 'cep' do modelo
        labels = {
            'cep': 'CEP'  # Personaliza o rótulo que aparece no template
        }
