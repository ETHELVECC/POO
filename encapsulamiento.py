###DEFINIR UNA CLASE CON MÉTODOS PÚBLICOS Y PRIVADOS
class Ejemplo:     #definida la clase con dos métodos
    def publico(self):   #método público 
        print('público')
    
    def __privado(self):  #método privado, lleva doble guión bajo al comienzo
        print('privado')

ej=Ejemplo()
ej.publico()       # da por resultado la impresión de la palabra Publico
ej.__privado()     # por consola arroja una excepción xq es privado

ej._Ejemplo__privado() #esto es el name mangling  se coloca el nombre de la clase y luego __nombre()
#y es posible acceder al método o atributo