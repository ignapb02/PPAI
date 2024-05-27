from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QMessageBox

class PantallaImportacionNovedades(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Importación de Novedades de Vinos')
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()
        
        self.label = QLabel('Bodegas Actualizables:')
        self.layout.addWidget(self.label)
        
        self.listaBodegas = QListWidget()
        self.layout.addWidget(self.listaBodegas)
        
        self.btnSeleccionar = QPushButton('Seleccionar Bodega')
        self.btnSeleccionar.clicked.connect(self.tomarBodegasSeleccionada)
        self.layout.addWidget(self.btnSeleccionar)

        self.setLayout(self.layout)

    def mostrarBodegasActualizables(self, bodegas):
        self.listaBodegas.clear()
        self.listaBodegas.addItems(bodegas)
    
    def tomarBodegasSeleccionada(self):
        selectedItems = self.listaBodegas.selectedItems()
        if not selectedItems:
            QMessageBox.warning(self, 'Advertencia', 'Seleccione una bodega.')
            return None
        return selectedItems[0].text()
