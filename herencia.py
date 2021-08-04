##Definir la clase Instrumento con sus métodos y atributos y creen clases 
##que hereden de ella

class Instrumento:                  ###clase general o super clase
    def __init__(self, precio):
        self.precio=precio
    
    def tocar(self):
        print('Estamos tocando Música')
    
    def precio(self):
        print('El precio de este instrumentos es: $', self.precio)

class Bateria(Instrumento):        #subclase que hereda los atributos de superclase
    pass

class Guitarra(Instrumento):       #subclase que hereda los atributos de superclase
    def __init__(self, tipo_cuerda, precio):     #se define un parámetro nuevo
        Instrumento.__init__(self, precio)       #se llama a la superclase con init
        self.tipo_cuerda = tipo_cuerda           #inicialización del parámetro
        

### Definir una clase Cocodrilo que herede las clases de acuatico y de terreste
### primero se define las clases terrestes y acuatico, luego la clase animal

class Terrestre:
    def __initi__(self):
        pass

    def desplazar(self):
        print('El animal anda')

class Acuatico:
    def __init__(self):
        pass
    
    def desplazar (self):
        print('El animal anda')

class Cocodrilo(Terrestre, Acuatico):  #Esta clase hereda las anteriores
    def __init__(self):
        Acuatico.__init__(self)

c = Cocodrilo()   #constructor de clase específica
c.desplazar()


##HERENCIA MULTINIVEL - Heredar de una clase derivada
##Definir diferentes clase con sus metodos y atributos
##luego implementar herencia multinivel entre ellas

class Figura:
    def __initi__(self, area):
        self.area=area
    
    def retornar_area(self):
        print('El área de la figura es:', self.area)

class Poligono(Figura):       #clase derivada de figura
    def __init__(self, lados, area):
        Figura.__init__(self, area)
        self.lados =lados
    
    def retornar_lados(self):
        print('los lados del poligono son:', self.lados)

class Cuadrilatero(Poligono):   #clase derivada de poligono
    def __init__(self, area):
        Poligono.__init__(self, 4, area)

#Esta clase tendrá los métodos y atributos de Poligono y Figura
#si en Poligono se redefine un método, cuadrilátero hereda redefinido

print(Cuadrilatero.__mro__) #ve como un atributo, devuelve por consola una tupla
print(Cuadrilatero.mro())   #ve como método devuelve una lista por consola