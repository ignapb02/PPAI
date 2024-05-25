class Bodega:
    def __init__(self, region, nombre, periodoActualizacion, historia, descripcion, coordUbi):
        self.region = region
        self.vinos = []
        self.nombre = nombre
        self.periodoActualizacion = periodoActualizacion #!
        self.historia = historia
        self.descripcion = descripcion
        self.coordUbi = []

    def addVino(self, vino):
        self.vinos.append(vino)

    def mostrarVinos(self):
        for vino in self.vinos:
            vino.mostrarVino(self)

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