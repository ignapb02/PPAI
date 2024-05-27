from Interface.InterfazApiBodega import InterfazApiBodega
from Interface.PantallaImportacionNovedades import PantallaImportacionNovedades

class GestorImportacionNovedades:
    def __init__(self, pantallaImportacionNovedades):
        self.bodegas = []
        self.bodegasActualizables = []
        self.nombreBodegasActualizables = []
        self.pantallaImportacionNovedades = pantallaImportacionNovedades

    def opcionImportarActualizacionVinos(self):
        self.buscarBodegasActualizables()
        self.pantallaImportacionNovedades.mostrarBodegasActualizables(self.nombreBodegasActualizables)
        bodegaSeleccionada = self.pantallaImportacionNovedades.tomarBodegasSeleccionada()
        if bodegaSeleccionada:
            actualizacionesVinos = self.obtenerActVinosBodegaSeleccionada(bodegaSeleccionada)
            self.obtenerVinosActualizables(bodegaSeleccionada)

    def buscarBodegasActualizables(self):
        for bodega in self.bodegas:
            if bodega.sePuedeActualizarNovedades():
                self.bodegasActualizables.append(bodega)
                self.nombreBodegasActualizables.append(bodega.getNombre())

    def obtenerActVinosBodegaSeleccionada(self, bodegaSeleccionada):
        return InterfazApiBodega().obtenerActualizacionesVinos(bodegaSeleccionada)

    def obtenerVinosActualizables(self, bodegaSeleccionada):
        pass

    def buscarActualizacionesVinos(self):
        pass

    def determinarVinosActualizar(self):
        pass

    def actualizarOCrearVinos(self):
        pass

    def actualizarVinoExistente(self):
        pass

    def crearVino(self):
        pass

    def buscarSeguidoresBodega(self):
        pass
