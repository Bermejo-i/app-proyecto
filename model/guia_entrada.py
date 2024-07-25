class guia_entrada:

    def __init__(self, codguiaentrada, fecha, codcliente, coddocventa, observaciones):
        self.codguiaentrada=codguiaentrada
        self.fecha=fecha
        self.coddocventa=coddocventa
        self.observaciones=observaciones
        self.codcliente=codcliente

    def set_codguiaentrada(self, codguiaentrada):
        self.codguiaentrada=codguiaentrada
    def set_fecha(self, fecha):
        self.fecha=fecha
    def set_coddocventa(self, coddocventa):
        self.coddocventa=coddocventa
    def set_observaciones(self, observaciones):
        self.observaciones=observaciones
    def set_codcliente(self, codcliente):
        self.codcliente=codcliente
        
    def get_codguiaentrada(self):
        return self.codguiaentrada
    def get_fecha(self):
        return self.fecha
    def get_coddocventa(self):
        self.coddocventa
    def get_observaciones(self):
        return self.observaciones
    def get_codcliente(self):
        return self.codcliente