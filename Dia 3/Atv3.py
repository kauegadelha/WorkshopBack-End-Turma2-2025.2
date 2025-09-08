"""
def somar(a, b):
    return a + b

resultado = somar(10, "5")
print(resultado)
"""

# tipo de operandos não suportado, um está em int e o outro em string
# Correção:

def somar(a, b):
    try:
        return a + b
    except TypeError:
        return 'Erro: tipo de operandos não suportado'

resultado = somar(10, "5")
print(resultado)