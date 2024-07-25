class detalle_guia_entrada:

    def __init__(self, codguiaentrada, codproducto, cantidad):
        self.codguiaentrada=codguiaentrada
        self.codproducto=codproducto
        self.cantidad=cantidad

    def set_codguiaentrada(self, codguiaentrada):
        self.codguiaentrada=codguiaentrada
    def set_codproducto(self, codproducto):
        self.codproducto=codproducto
    def set_cantidad(self, cantidad):
        self.cantidad=cantidad
        
    def get_codguiaentrada(self):
        return self.codguiaentrada
    def get_codproducto(self):
        return self.codproducto
    def get_cantidad(self):
        self.cantidad