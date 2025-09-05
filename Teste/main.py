import FiguraGeometrica
def menu():
    print('\n===============================================')
    print('| OP [1]: Calcular a área de um circulo         |')
    print('| OP [2]: Calcular a área de um triângulo       |')
    print('| OP [3]: Calcular a hipotenusa de um triângulo |')
    print('| OP [4]: Sair.                                 |')
    print('=================================================')
loop = True
while loop == True:
    menu()
    opcao = int(input('\nDigite uma opção: '))
    if opcao == 1:
        raio = float(input('\nDigite o raio do circulo: '))
        print(FiguraGeometrica.Calc.area_circulo(raio))
    elif opcao == 2:
        base = float(input('\nDigite a base do triângulo: '))
        altura = float(input('Digite a altura do triângulo: '))
        print(FiguraGeometrica.Calc.area_triangulo(base, altura))
    elif opcao == 3:
        catet1 = float(input('\nDigite o tamanho do cateto 1: '))
        catet2 = float(input('Digite o tamanho do cateto 2: '))
        print(FiguraGeometrica.Calc.hipotenuza_triangulo(catet1, catet2))
    elif opcao == 4:
        loop = False
        print('\nSaindo...')
    else:
        print('\nOpção inválida!')