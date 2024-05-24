class Enofilo():
    def __init__(self,apellido=str(),nombre=str(),imagen= None):
        self.apellido = apellido
        self.nombre = nombre 
        self.imagen = imagen 
        self.siguiendo = []
        self.coleccionFavoritos = []

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