class detalle_factura_compra:

    def __init__(self, codfacturacompra, codinsumo, precio, cantidad):
        self.codfacturacompra=codfacturacompra
        self.codinsumo=codinsumo
        self.precio=precio
        self.cantidad=cantidad

    def set_codfacturacompra(self, codfacturacompra):
        self.codfacturacompra=codfacturacompra
    def set_codinsumo(self, codinsumo):
        self.codinsumo=codinsumo
    def set_precio(self, precio):
        self.precio=precio
    def set_cantidad(self, cantidad):
        self.cantidad=cantidad
        
    def get_codfacturacompra(self):
        return self.codfacturacompra
    def get_codinsumo(self):
        return self.codinsumo
    def get_precio(self):
        return self.codproducto
    def get_cantidad(self):
        self.cantidad