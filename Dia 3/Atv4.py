"""
numeros = [10, 20, 30]
indice = int(input("Digite um índice para acessar a lista: ")) 

print(numeros[indice])
"""
# Correção:
def verificar_indice(indice: int):
    if indice < 0 or indice > 2:
        return 'Índice inválido!'
    else:
        return indice

numeros = [10, 20, 30]

try:
    entrada = int(input('Digite um índice para acessar a lista: '))
    verificador = verificar_indice(entrada)

    if isinstance(verificador, int):
        print(numeros[verificador])
    else:
        print(verificador)
except ValueError:
    print('Erro: valor incompatível, requer um número inteiro.')