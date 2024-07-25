class venta_detalle:

    def __init__(self, codpedidoventa, codproducto, precioventa, cantidad):
        self.codpedidoventa=codpedidoventa
        self.codproducto=codproducto
        self.precioventa=precioventa
        self.cantidad=cantidad

    def set_codpedidoventa(self, codpedidoventa):
        self.codpedidoventa=codpedidoventa
    def set_codproducto(self, codproducto):
        self.codproducto=codproducto
    def set_precioventa(self, precioventa):
        self.precioventa=precioventa
    def set_cantidad(self, cantidad):
        self.cantidad=cantidad
    
    def get_codpedidoventa(self):
        return self.codpedidoventa
    def get_codproducto(self):
        return self.codproducto
    def get_precioventa(self):
        self.precioventa
    def get_cantidad(self):
        return self.cantidad