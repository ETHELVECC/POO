#ejemplo de Herencia   
#caso 1 de desafios

class Vehiculo():      #clase base
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return 'Color {}, {} ruedas'. format(self.color, self.ruedas)


class Coche(Vehiculo):   #clase derivada (Pone el nombre de la clase padre)
    def __init__(self, color, ruedas, velocidad, cilindrada): 
        Vehiculo.__init__(self, color, ruedas) ##inicializa la clase padre
        self.velocidad = velocidad              ##define las nuevas para la clase hijo
        self.cilindrada = cilindrada
    
    def __str__(self):
        return Vehiculo.__str__(self) + ', {} km/h, {} cc'. format(self.velocidad, self.cilindrada)

c = Coche('Azul', 4, 150, 1200)
print(c)


