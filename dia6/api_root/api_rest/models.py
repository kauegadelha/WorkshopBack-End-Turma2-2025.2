from django.db import models

# Create your models here.

class Endereco(models.Model): 
#Cada atributo da classe vira uma coluna na tabela do banco de dados.
#A classe não cria o banco sozinha, ela só diz como ele deve ser.
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)

    # Esse método define como o objeto será exibido em textos.
    def __str__(self):
        return f" Rua: {self.rua}, Bairro: {self.bairro}, Cidade: {self.cidade}, Estado: {self.estado}, Cep: {self.cep}."

