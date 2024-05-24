class Enofilo():
    def __init__(self,apellido=str(),nombre=str(),imagen= None):
        self.apellido = apellido
        self.nombre = nombre 
        self.imagen = imagen 
        self.siguiendo = []
        self.coleccionFavoritos = []


    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setNombre(self,nombre):
        self.nombre = nombre
    
    def setImagen(self, imagen):
        self.imagen = imagen
    
    def getApellido(self):
        return self.apellido
    
    def getNombre(self):
        return self.nombre
    
    def getImagen (self):
        return self.imagen

    def getSiguiendo(self):
        return self.siguiendo
    
    def getColeccionFavoritos(self):
        return self.coleccionFavoritos
    
#Metodos de Pantalla
    def mostrarAmigosSeguidos(self):
        if self.siguiendo:
            print("Amigos seguidos:")
            for amigo in self.siguiendo:
                print(amigo)
        else:
            print("El enofilo no tiene amigos seguidos")

    def mostrarColeccionFavoritos(self):
        if self.coleccionFavoritos:
            print("Coleccion de Favoritos:")
            for favorito in self.coleccionFavoritos:
                print(favorito)
        else:
            print("El enofilo no tiene ningun vino favorito")