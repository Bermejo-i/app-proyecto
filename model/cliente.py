class cliente:

    def __init__(self, codcliente , telefono, direccion, correo, codtipocliente, nombres, apellidos):
        self.codcliente=codcliente
        self.telefono=telefono
        self.direccion=direccion
        self.correo=correo
        self.codtipocliente=codtipocliente
        self.nombres=nombres
        self.apellidos=apellidos

    def set_codcliente(self, codcliente):
        self.codcliente=codcliente
    def set_telefono(self, telefono):
        self.telefono=telefono
    def set_direccion(self, direccion):
        self.direccion=direccion
    def set_correo(self, correo):
        self.correo=correo
    def set_codtipocliente(self, codtipocliente):
        self.codtipocliente=codtipocliente
    def set_nombres(self, nombres):
        self.nombres=nombres
    def set_apellidos(self, apellidos):
        self.apellidos=apellidos
    
    def get_codcliente(self):
        return self.codcliente
    def get_telefono(self):
        self.telefono
    def get_direccion(self):
        return self.direccion
    def get_correo(self):
        return self.correo
    def get_codtipocliente(self):
        return self.codtipocliente
    def get_nombres(self):
        self.nombres
    def get_apellidos(self):
        self.apellidos