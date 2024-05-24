from enofilo import *
from bodega import *


class Siguiendo():
    def __init__(self,fechaInicio=None,fechaFin=None):
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.enofilo = Enofilo()
        self.bodega = Bodega()

    def setFechaInicio(self,fechaInicio):
        self.fechaInicio = fechaInicio

    def setFechaFin(self,fechaFin):
        self.fechaFin = fechaFin

    def getfechaInicio(self):
        return self.fechaInicio

    def getfechaFin(self):
        return self.fechaFin
    
    def sosBodega():
        pass