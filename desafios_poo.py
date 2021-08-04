#caso 2 de desafios
#Crea al menos un objeto de cada subclase y añadelos a una lista llamada vehiculos.
#Realiza una función llamada catalogar() que reciba la lista de vehículos 
# y los recorra mostrando el nombre de su clase y sus atributos.
#Modifica la función catalogar() para que reciba un argumento optativo ruedas,
# haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. 
# También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente si se envía el argumento ruedas. 
# Ponla a prueba con 0, 2 y 4 ruedas como valor.

from typing_extensions import ParamSpecArgs


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

class Bicicleta(Vehiculo):
    pass

class Motocicleta(Vehiculo):
    pass

class Camioneta(Vehiculo):
    pass


def catalogar():
    pass



c = Coche('Azul', 4, 150, 1200)
print(c)