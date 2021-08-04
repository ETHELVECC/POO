##Definir una clase con atribuos privado y sus métodos getters y setters

class Fecha():
    def __init__(self):
        self.__dia = 1
    
    def getDia(self):          #método get
        return self.__dia
    
    def setDia(self, dia):    #método set
        if dia > 0 and dia < 31:
            self.__dia =dia
        else:
            print('Error')

    dia = property(getDia, setDia)

mi_fecha = Fecha()

# mi_fecha.setDia(30)       #método set me da error xq no se encuentra dentro de las condiciones del if

# mi_fecha.__dia = 30        #me devuelve 1, donde se inicializa(init)
# print(mi_fecha.getDia())
mi_fecha.dia=30
print(mi_fecha.dia)  