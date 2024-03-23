class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Hola, estoy hablando un poco")
    
class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"
        
class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
        
    def presentarse(self):
       print(f"hola, soy: {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}")
        
class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,notas,universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.notas = notas
        self.universidad = universidad




roberto = EmpleadoArtista("Roberto",43,"Argentino","cantar","Programador",1000000000)

herencia = issubclass(EmpleadoArtista,Persona)
instancia = isinstance(roberto,EmpleadoArtista)

print(instancia)  