##Definir una clase con sus métodos y atributos implementando sobrecarga de métodos

# class Persona():
#     def __init__(self,cedula):
#         self.cedula = cedula
    
#     def mensaje(self):
#         print('Mensaje desde la clase Persona')

# class Obrero(Persona):    #Hereda desde la clase persona
#     def __init__(self,cedula):
#         Persona.__init__(self,cedula)
#         self.__especialista = 1
    
#     def mensaje(self):
#         print('Mensaje desde la clase obrera')

# obrero_planta = Obrero(12345)
# obrero_planta.mensaje()


##Definir una clase con sus métodos y atributos implementando sobrecarga de operdores
class Punto:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    
    def __add__(self, other):    #sobre carga de operadores
        x=self.x + other.x
        y=self.y + other.y
        return (x,y)

punto1=Punto(4,6)
punto2=Punto(1,-2)
print(punto1+punto2)