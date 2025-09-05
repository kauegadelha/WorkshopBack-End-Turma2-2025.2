class Animal():
    def __init__(self,nome = '', idade = 0):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return 'Som genérico' 
    
    def setNome(self, nome):
        self.nome = nome
    
    def setIdade(self, idade):
        self.idade = idade
        
    def apresentar(self):
        return f'nome: {self.nome}  idade: {self.idade}'

    
class Gato(Animal):
    def falar(self):
        return 'Miau!'

class Cachorro(Animal):
    def falar(self):
        return 'Au au!'

class Zoologico:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def listar_animais(self):
        return [f'{a.apresentar()} Faz: {a.falar()}' for a in self.animais]
    
    def filtrar_por_tipo(self, tipo):
        return [a for a in self.animais if isinstance(a, tipo)]
    
animal = Animal()
gato = Gato()
cachorro = Cachorro()

print(animal.falar())
print(gato.falar())
print(cachorro.falar())

gato.setNome('Felix')
gato.setIdade(3)

print(gato.apresentar())

nome = input('Digite o nome do animal: ')
idade = int(input('Digite a idade do animal: '))

gato = Gato(nome, idade)
print(gato.apresentar())