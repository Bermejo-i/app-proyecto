class inventario:

    def __init__(self, codinventario, descripcion, codguiaentrada, codguiasalida, stockinicial, totalstock):
        self.codinventario=codinventario
        self.descripcion=descripcion
        self.codguiaentrada=codguiaentrada
        self.codguiasalida=codguiasalida
        self.stockinicial=stockinicial
        self.totalstock=totalstock

    def set_codinventario(self, codinventario):
        self.codinventario=codinventario
    def set_descripcion(self, descripcion):
        self.descripcion=descripcion
    def set_codguiaentrada(self, codguiaentrada):
        self.codguiaentrada=codguiaentrada
    def set_codguiasalida(self, codguiasalida):
        self.codguiasalida=codguiasalida
    def set_stockinicial(self, stockinicial):
        self.stockinicial=stockinicial
    def set_totalstock(self, totalstock):
        self.totalstock=totalstock
        
    def get_codinventario(self):
        return self.codinventario
    def get_descripcion(self):
        return self.descripcion
    def get_codguiaentrada(self):
        self.codguiaentrada
    def get_codguiasalida(self):
        return self.codguiasalida
    def get_stockinicial(self):
        return self.stockinicial
    def get_totalstock(self):
        self.totalstock