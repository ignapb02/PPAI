import sys
from PyQt5.QtWidgets import QApplication
from Interface.PantallaImportacionNovedades import PantallaImportacionNovedades
from Controllers.GestorImportacionNovedades import GestorImportacionNovedades

class MockBodega:
    def __init__(self, nombre, se_puede_actualizar):
        self.nombre = nombre
        self.se_puede_actualizar = se_puede_actualizar

    def sePuedeActualizarNovedades(self):
        return self.se_puede_actualizar

    def getNombre(self):
        return self.nombre

if __name__ == '__main__':
    # Crear una instancia de QApplication antes de cualquier widget
    app = QApplication(sys.argv)
    
    # Crear la instancia de la pantalla
    pantalla = PantallaImportacionNovedades()
    
    # Crear la instancia del gestor
    gestor = GestorImportacionNovedades(pantalla)
    
    # Simular algunas bodegas
    gestor.bodegas = [
        MockBodega("Bodega 1", True),
        MockBodega("Bodega 2", False),
        MockBodega("Bodega 3", True)
    ]

    # Mostrar la pantalla y ejecutar el método del gestor
    pantalla.show()
    gestor.opcionImportarActualizacionVinos()

    # Ejecutar el loop de la aplicación
    sys.exit(app.exec_())
