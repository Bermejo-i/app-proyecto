class insumos:

    def __init__(self, codinsumo, codcompra, stock, descripcion, precio, codproveedor):
        self.codinsumo=codinsumo
        self.descripcion=descripcion
        self.codcompra=codcompra
        self.stock=stock
        self.precio=precio
        self.codproveedor=codproveedor

    def set_codinsumo(self, codinsumo):
        self.codinsumo=codinsumo
    def set_descripcion(self, descripcion):
        self.descripcion=descripcion
    def set_codcompra(self, codcompra):
        self.codcompra=codcompra
    def set_stock(self, stock):
        self.stock=stock
    def set_precio(self, precio):
        self.precio=precio
    def set_codproveedor(self, codproveedor):
        self.codproveedor=codproveedor
        
    def get_codinsumo(self):
        return self.codinsumo
    def get_descripcion(self):
        return self.descripcion
    def get_codcompra(self):
        self.codcompra
    def get_stock(self):
        return self.stock
    def get_precio(self):
        return self.precio
    def get_codproveedor(self):
        self.codproveedor