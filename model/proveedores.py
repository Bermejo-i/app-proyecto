class proveedores:

    def __init__(self, ruc, codproveedor, representante, rubro, telefono, direccion, correo, nombre, apellidos):
        self.ruc=ruc
        self.codproveedor=codproveedor
        self.representante=representante
        self.rubro=rubro
        self.telefono=telefono
        self.direccion=direccion
        self.correo=correo
        self.nombre=nombre
        self.apellidos=apellidos

    def set_ruc(self, ruc):
        self.ruc=ruc
    def set_codproveedor(self, codproveedor):
        self.codproveedor=codproveedor
    def set_representante(self, representante):
        self.representante=representante
    def set_direccion(self, direccion):
        self.direccion=direccion
    def set_correo(self, correo):
        self.correo=correo
    def set_rubro(self, rubro):
        self.rubro=rubro
    def set_telefono(self, telefono):
        self.telefono=telefono
    def set_nombre(self, nombre):
        self.nombre=nombre
    def set_apellidos(self, apellidos):
        self.apellidos=apellidos
        
        
    
    def get_codproveedor(self):
        return self.codproveedor
    def get_ruc(self):
        return self.ruc
    def get_telefono(self):
        self.telefono
    def get_direccion(self):
        return self.direccion
    def get_correo(self):
        return self.correo
    def get_representante(self):
        return self.representante
    def get_rubro(self):
        return self.rubro
    def get_nombre(self):
        return self.nombre
    def get_apellidos(self):
        return self.apellidos