from django.shortcuts import render
from .forms import ViaCepForm
from .models import Endereco
from django.views.generic import FormView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
import requests

def home(request):
    # Renderiza o template 'home.html', que deve conter o formulário para o usuário digitar o CEP
    return render(request, 'app/home.html') 

def consulta_cep(request):
    return render (request, 'app/consulta_cep.html')

# FormView de Via Cep
class ViaCepFormView(FormView):
    template_name = 'crud/create.html'   # recomendo criar essa pasta "crud"
    form_class = ViaCepForm
    success_url = reverse_lazy('viacep:list')  # depois de salvar, redireciona para lista

    def form_valid(self, form):
        cep = form.cleaned_data['cep']
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url, verify=False)

        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                # salvar ou atualizar no banco
                cep_obj, created = Endereco.objects.update_or_create(
                    cep = cep,
                    defaults={
                        "rua": data.get("logradouro", ""),
                        "bairro": data.get("bairro", ""),
                        "cidade": data.get("localidade", ""),
                        "estado": data.get("uf", ""),
                    }
                )
                self.object = cep_obj
            else:
                form.add_error("cep", "CEP não encontrado na API do ViaCEP.")
                return self.form_invalid(form)
        else:
            form.add_error("cep", "Erro ao consultar a API do ViaCEP.")
            return self.form_invalid(form)
        
        return super().form_valid(form)

# Lista de todos os CEPs
class ViaCepListView(ListView):
    model = Endereco
    template_name = "crud/list.html"
    context_object_name = "ceps"

# Detalhe de 1 CEP
class ViaCepDetailView(DetailView):
    model = Endereco
    template_name = "crud/detail.html"
    context_object_name = "cep"

# Excluir um CEP
class ViaCepDeleteView(DeleteView):
    model = Endereco
    template_name = "crud/delete.html"
    success_url = reverse_lazy("viacep:list")
