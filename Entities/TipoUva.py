class TipoUva:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def sosTipoUva(self, busqueda):
        return self.nombre == busqueda
    
    def getDescripcion(self):
        return self.descripcion
    
    def getNombre(self):
        return self.nombre
    
    def setDescripcion(self, valor=str()):
        self.descripcion = valor

    def setNombre(self, valor=str()):
        self.nombre = valor