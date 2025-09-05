import math
class Calc():
    def area_circulo(raio: float) -> float:
        area = math.pi * pow(raio, 2)
        return area
    def area_triangulo(base: float, altura: float) -> float:
        area = (base * altura)/2
        return area
    def hipotenuza_triangulo(catet1: float, catet2: float) -> float:
        hipotenuza = math.sqrt(catet1 **2 + catet2 **2)
        return hipotenuza

