class documento_venta:

    def __init__(self, codfacturacompra, fecha, codproveedor, tipodoc, igv, subtotal, totalfactura, observaciones):
        self.codfacturacompra=codfacturacompra
        self.codproveedor=codproveedor
        self.tipodoc=tipodoc
        self.fecha=fecha
        self.igv=igv
        self.subtotal=subtotal
        self.totalfactura=totalfactura
        self.observaciones=observaciones

    def set_codfacturacompra(self, codfacturacompra):
        self.codfacturacompra=codfacturacompra
    def set_codproveedor(self, codproveedor):
        self.codproveedor=codproveedor
    def set_tipodoc(self, tipodoc):
        self.tipodoc=tipodoc
    def set_fecha(self, fecha):
        self.fecha=fecha
    def set_igv(self, igv):
        self.igv=igv
    def set_subtotal(self, subtotal):
        self.subtotal=subtotal
    def set_totalfactura(self, totalfactura):
        self.totalfactura=totalfactura
    def set_observaciones(self, observaciones):
        self.observaciones=observaciones
    
    def get_codfacturacompra(self):
        return self.codfacturacompra
    def get_codproveedor(self):
        return self.codproveedor
    def get_tipodoc(self):
        self.tipodoc
    def get_fecha(self):
        return self.fecha
    def get_igv(self):
        return self.igv
    def get_subtotal(self):
        self.subtotal  
    def get_totalfactura(self):
        self.totalfactura
    def get_observaciones(self):
        self.observaciones 