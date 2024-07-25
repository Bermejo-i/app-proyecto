class producto:

    def __init__(self, codproducto, nombre, codcategoria, fvenc, stockmin, stockmax, estado):
        self.codproducto=codproducto
        self.nombre=nombre
        self.codcategoria=codcategoria
        self.fvenc=fvenc
        self.stockmin=stockmin
        self.stockmax=stockmax
        self.estado=estado

    def set_codproducto(self, codproducto):
        self.codproducto=codproducto
    def set_nombre(self, nombre):
        self.nombre=nombre
    def set_codcategoria(self, codcategoria):
        self.codcategoria=codcategoria
    def set_fvenc(self, fvenc):
        self.fvenc=fvenc
    def set_stockmin(self, stockmin):
        self.stockmin=stockmin
    def set_stockmax(self, stockmax):
        self.stockmax=stockmax
    def set_estado(self, estado):
        self.estado=estado
    
    def get_codproducto(self):
        return self.codproducto
    def get_nombre(self):
        return self.nombre
    def get_codcategoria(self):
        self.codcategoria
    def get_fvenc(self):
        return self.fvenc
    def get_stockmin(self):
        return self.stockmin
    def get_stockmax(self):
        self.stockmax
    def get_estado(self):
        self.estado 