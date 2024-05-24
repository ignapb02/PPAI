class Bodega:
    def __init__(self, descripcion=str(), ubicacion=str(), historia=str(), 
                 nombre=str(), periodoActualizacion=int()):
        
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.historia = historia
        self.nombre = nombre
        self.periodoActuaizacion = periodoActualizacion
        self.fechaUltimaActualizacion = None
    
    # Metodos get para cada atributo
    def getDescripcion(self):
        return self.descripcion
    
    def getUbicacion(self):
        return self.ubicacion
    
    def getHistoria(self):
        return self.historia
    
    def getNombre(self):
        return self.nombre
    
    def getPeriodoActualizacion(self):
        return self.periodoActuaizacion
    
    def getFechaUltActualizacion(self):
        return self.fechaUltimaActualizacion

    # Métodos set para cada atributo
    def setDescripcion(self, valor):
        self.descripcion = valor

    def setUbicacion(self, valor):
        self.ubicacion = valor

    def setHistoria(self, valor):
        self.historia = valor

    def setNombre(self, valor):
        self.nombre = valor

    def setFechaUltActualizacoin(self, valor):
        self.fechaUltimaActualizacion = valor

    def setPeriodoActualizacion(self, valor):
        self.periodoActuaizacion = valor