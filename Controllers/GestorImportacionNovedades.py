class GestorImportacionNovedades:

    def __init__(self):
        self.bodegas = []
        self.bodegasActualizables = []
        self.NombreBodegasActualizables = []

    def opcionImportarActualizacionVinos(self):
        pass


    def BuscarBodegasActualizables(self):

        #Busca desde las bodegas que estan en periodo de actualizacion, las guarda en la lista bodegasActualizables junto a su nombre
        # en la lista NombreBodegasActualizables (los cuales deberian tener el mismo indice)

        for bodega in self.bodegas:

            if bodega.sePuedeActualizarNovedades():
                self.bodegasActualizables.append(bodega)
                self.NombreBodegasActualizables.append(bodega.getNombre())

    def buscarActualizacionesVinos():
        pass

    def determinarVinosActualizar():
        pass

    def actualizarOCrearVinos():
        pass

    def actualizarVinoExistente():
        pass

    def crearVino():
        #vino = Vino(bodega, nombre, random.randint(2000, 2024), None, random.randint(2000,5000))
        pass

    def buscarSeguidoresBodega():
        pass