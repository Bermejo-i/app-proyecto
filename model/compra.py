class compra:

    def __init__(self,codcompra, fecha, hora, codproveedor, codinsumos):
        self.codcompra=codcompra
        self.fecha=fecha
        self.hora=hora
        self.codproveedor=codproveedor
        self.codinsumos=codinsumos

    def set_codcompra(self, codcompra):
        self.codcompra=codcompra
    def set_fecha(self, fecha):
        self.fecha=fecha
    def set_hora(self, hora):
        self.hora=hora
    def set_codproveedor(self, codproveedor):
        self.codproveedor=codproveedor
    def set_codinsumos(self, codinsumos):
        self.codinsumos=codinsumos
    
    def get_codcompra(self):
        return self.codcompra
    def get_fecha(self):
        return self.fecha
    def get_hora(self):
        self.hora
    def get_codproveedor(self):
        return self.codproveedor
    def get_codinsumos(self):
        return self.codinsumos