class tipo_trabajador:

    def __init__(self, idtipotrabajador, descripcion):
        self.idtipotrabajador=idtipotrabajador
        self.descripcion=descripcion

    def set_idtipotrabajador(self, idtipotrabajador):
        self.idtipotrabajador=idtipotrabajador
    def set_descripcion(self, descripcion):
        self.descripcion=descripcion
    
    def get_idtipotrabajador(self):
        return self.idtipotrabajador
    def get_descripcion(self):
        return self.descripcion
