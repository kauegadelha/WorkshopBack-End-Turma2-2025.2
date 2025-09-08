"""
def dividir(a, b):
    return a / b

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

resultado = dividir(int(num1), int(num2))
print(f"Resultado: {resultado}")
"""

# Correção:
def dividir(a, b):
    try:
        a = int(a)
        b = int(b)
        return a / b
    except ValueError:
        return 'Erro: valores incompatíveis'
    except ZeroDivisionError:
        return 'Erro: não é possivel dividir por zero'

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

resultado = dividir(num1, num2)
if isinstance(resultado, int):
    print(f"Resultado: {resultado}")
else:
    print(resultado)

# Erros gerados: tipo incompatível se digitar letra, se o segundo número for 0, a divisão da erro