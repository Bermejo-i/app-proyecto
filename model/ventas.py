class ventas:

    def __init__(self, codventa, fecha, hora, codproductos, codcliente):
        self.codventa=codventa
        self.fecha=fecha
        self.hora=hora
        self.codproductos=codproductos
        self.codcliente=codcliente

    def set_codventa(self, codventa):
        self.codventa=codventa
    def set_fecha(self, fecha):
        self.fecha=fecha
    def set_hora(self, hora):
        self.hora=hora
    def set_codproductos(self, codproductos):
        self.codproductos=codproductos
    def set_codcliente(self, codcliente):
        self.codcliente=codcliente
        
    def get_codventa(self):
        return self.codventa
    def get_fecha(self):
        return self.fecha
    def get_hora(self):
        self.hora
    def get_codproductos(self):
        return self.codproductos
    def get_codcliente(self):
        return self.codcliente