from django.db import models

# Create your models here.

class Endereco(models.Model):
    cep = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return f" RUA: {self.rua}, Bairro: {self.bairro}, Cidade: {self.cidade}, Estado: {self.estado}."