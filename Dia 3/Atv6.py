"""
dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}

chave = input("Digite a chave que deseja acessar: ")

print(f"O valor da chave '{chave}' é: {dados[chave]}")
"""
# Correção:
dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}
try: 
    chave = str(input("Digite a chave que deseja acessar: ")).strip()
    print(f"O valor da chave '{chave}' é: {dados[chave]}")
except KeyError:
    print("Erro: chave não encontrada")

# usando o método get():
"""
dados = {
    "nome": "Isaac",
    "idade": 25,
    "cidade": "São Paulo"
}

chave = input("Digite a chave que deseja acessar: ").strip()
valor = dados.get(chave, "Chave não encontrada")
print(f"O valor da chave '{chave}' é: {valor}")
"""