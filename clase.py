class Persona:
    def __init__(self, nombre, edad, genero, estatura, peso):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.estatura=estatura
        self.peso=peso

    def hablar(self):
        print('hola soy {}'.format(self.nombre))
    
    def correr(self):
        print('{} está corriendo'.format(self.nombre))

    def caminar(self):
        print('{} está caminando'.format(self.nombre))

#definimos los objetos persona 1 y 2, con 1 parámetro menos, es decir sin usar el self
persona1=Persona('Juan', 23, 'masculino', 1.7, 90) 
persona2=Persona('María', 25,'femenino', 1.65, 70)

persona1.hablar() #se llama a la función hablar para la persona 1
persona2.caminar() #llama la funcion caminar para la persona 2
print(persona1.genero)  #se accede a los atributos de  objeto