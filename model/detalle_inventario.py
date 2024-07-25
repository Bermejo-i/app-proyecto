class detalle_inventario:

    def __init__(self, codinventario, codinsumo, cantidad):
        self.codinventario=codinventario
        self.codinsumo=codinsumo
        self.cantidad=cantidad

    def set_codinventario(self, codinventario):
        self.codinventario=codinventario
    def set_codinsumo(self, codinsumo):
        self.codinsumo=codinsumo
    def set_cantidad(self, cantidad):
        self.cantidad=cantidad
        
    def get_codinventario(self):
        return self.codinventario
    def get_codinsumo(self):
        return self.codinsumo
    def get_cantidad(self):
        self.cantidad