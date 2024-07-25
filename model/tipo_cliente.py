class tipo_cliente:

    def __init__(self, codtipocliente, descripcion):
        self.codtipocliente=codtipocliente
        self.descripcion=descripcion

    def set_codtipocliente(self, codtipocliente):
        self.idtipotrabajador=codtipocliente
    def set_descripcion(self, descripcion):
        self.descripcion=descripcion
    
    def get_codtipocliente(self):
        return self.codtipocliente
    def get_descripcion(self):
        return self.descripcion
