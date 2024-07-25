class detalle_guia_salida:

    def __init__(self, codguiasalida, codproducto, cantidad):
        self.codguiasalida=codguiasalida
        self.codproducto=codproducto
        self.cantidad=cantidad

    def set_codguiasalida(self, codguiasalida):
        self.codguiasalida=codguiasalida
    def set_codproducto(self, codproducto):
        self.codproducto=codproducto
    def set_cantidad(self, cantidad):
        self.cantidad=cantidad
        
    def get_codguiasalida(self):
        return self.codguiasalida
    def get_codproducto(self):
        return self.codproducto
    def get_cantidad(self):
        self.cantidad