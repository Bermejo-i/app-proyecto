class categoria:

    def __init__(self, codCategoria, descripcion):
        self.codCategoria=codCategoria
        self.descripcion=descripcion

    def set_codCategoria(self, codCategoria):
        self.codCategoria=codCategoria
    def set_descripcion(self, descripcion):
        self.descripcion=descripcion
    
    def get_codCategoria(self):
        return self.codCategoria
    def get_descripcion(self):
        return self.descripcion
