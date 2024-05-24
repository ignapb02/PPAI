class TipoUvas():
    def __init__(self, descripcion=str(), nombre=str()):
        self.descripcion = descripcion
        self.nombre = nombre

    def getDescripcion(self):
        return self.descripcion
    
    def getNombre(self):
        return self.nombre
    
    def setDescripcion(self, valor=str()):
        self.descripcion = valor

    def setNombre(self, valor=str()):
        self.nombre = valor