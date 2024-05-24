from tipoUva import *

class Varietal():
    def __init__(self, descripcion=str(), porcentajeUva=float(), tipoUva=TipoUvas()):
        self.descripcion = descripcion
        self.porcentajeUva = porcentajeUva
        self.tipoUva = tipoUva
    
    def getDescripcion(self):
        return self.descripcion
    
    def getPorcentajeUva(self):
        return self.porcentajeUva
    
    def getTipoUva(self):
        return self.porcentajeUva
    
    def setDescripcion(self, valor=str()):
        self.descripcion = valor

    def setPorcentajeUva(self, valor=float()):
        self.porcentajeUva = valor

    def setTipoUva(self, valor=TipoUvas()):
        self.tipoUva = valor