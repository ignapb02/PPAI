from varietal import *
from maridaje import *

class Vino:
    def __init__(self, añada, etiqueta, nombre=str(), notaDeCata=str(), precio=float()):
        self.varietal = Varietal()
        self.maridaje = Maridaje()
        self.añada = añada
        self.nombre = nombre
        self.notaDeCata = notaDeCata
        self.etiqueta = etiqueta
        self.precio = precio


    