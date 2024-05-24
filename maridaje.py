class Maridaje():
    def __init__(self,nombre=str(), descripcion=str()):
        self.nombre = nombre
        self.descripcion = descripcion

    def setMaridaje(self,nombre,descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def getNombreMaridaje(self):
        return self.nombre
       
    def getDescripcionMaridaje(self):
        return self.descripcion