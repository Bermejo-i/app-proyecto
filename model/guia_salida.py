class guia_salida:

    def __init__(self, codguiasalida, fecha, codcliente, coddocventa, observaciones):
        self.codguiasalida=codguiasalida
        self.fecha=fecha
        self.coddocventa=coddocventa
        self.observaciones=observaciones
        self.codcliente=codcliente

    def set_codguiasalida(self, codguiasalida):
        self.codguiasalida=codguiasalida
    def set_fecha(self, fecha):
        self.fecha=fecha
    def set_coddocventa(self, coddocventa):
        self.coddocventa=coddocventa
    def set_observaciones(self, observaciones):
        self.observaciones=observaciones
    def set_codcliente(self, codcliente):
        self.codcliente=codcliente
        
    def get_codguiasalida(self):
        return self.codguiasalida
    def get_fecha(self):
        return self.fecha
    def get_coddocventa(self):
        self.coddocventa
    def get_observaciones(self):
        return self.observaciones
    def get_codcliente(self):
        return self.codcliente