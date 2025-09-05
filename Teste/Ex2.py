import math

def arredondamentos(numero: float) -> dict:
    return {
        "piso" : math.floor(numero),
        "teto" : math.ceil(numero),
        "arredondado" : round(numero)
    }

numero = float(input('Digite um número: '))
arredondamentos(numero)
