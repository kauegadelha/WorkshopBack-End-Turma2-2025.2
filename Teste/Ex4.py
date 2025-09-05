class Animal():
    def falar(self):
        return 'Som genérico' 
    
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