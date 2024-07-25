class documento_venta:

    def __init__(self, codventa, codpedidoventa, tipodocventa, fecha, igv, subtotal, montototal):
        self.codventa=codventa
        self.codpedidoventa=codpedidoventa
        self.tipodocventa=tipodocventa
        self.fecha=fecha
        self.igv=igv
        self.subtotal=subtotal
        self.montototal=montototal

    def set_codventa(self, codventa):
        self.codventa=codventa
    def set_codpedidoventa(self, codpedidoventa):
        self.codpedidoventa=codpedidoventa
    def set_tipodocventa(self, tipodocventa):
        self.tipodocventa=tipodocventa
    def set_fecha(self, fecha):
        self.fecha=fecha
    def set_igv(self, igv):
        self.igv=igv
    def set_subtotal(self, subtotal):
        self.subtotal=subtotal
    def set_montototal(self, montototal):
        self.montototal=montototal
    
    def get_codventa(self):
        return self.codventa
    def get_codpedidoventa(self):
        return self.codpedidoventa
    def get_tipodocventa(self):
        self.tipodocventa
    def get_fecha(self):
        return self.fecha
    def get_igv(self):
        return self.igv
    def get_subtotal(self):
        self.subtotal  
    def get_montototal(self):
        self.montototal 