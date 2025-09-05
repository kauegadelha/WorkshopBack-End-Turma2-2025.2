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
    
animal = Animal()
gato = Gato()
cachorro = Cachorro()

print(animal.falar())
print(gato.falar())
print(cachorro.falar())

gato.setNome('Felix')
gato.setIdade(3)
print(gato.apresentar)
