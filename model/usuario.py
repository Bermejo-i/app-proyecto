class usuario:

    def __init__(self,cod_trab,tipoTrab,telefono,direccion,correo,edad,cargo):
        self.cod_trab=cod_trab
        self.tipoTrab=tipoTrab
        self.telefono=telefono
        self.direccion=direccion
        self.correo=correo
        self.edad=edad
        self.cargo=cargo

    def set_cod_trab(self, cod_trab):
        self.cod_trab=cod_trab
    def set_tipoTrab(self, tipoTrab):
        self.tipoTrab=tipoTrab
    def set_telefono(self, telefono):
        self.telefono=telefono
    def set_direccion(self, direccion):
        self.direccion=direccion
    def set_correo(self, correo):
        self.correo=correo
    def set_edad(self, edad):
        self.edad=edad
    def set_cargo(self, cargo):
        self.cargo=cargo
    
    def get_cod_trab(self):
        return self.cod_trab
    def get_tipoTrab(self):
        return self.tipoTrab
    def get_telefono(self):
        self.telefono
    def get_direccion(self):
        return self.direccion
    def get_correo(self):
        return self.correo
    def get_edad(self):
        self.edad  
    def get_cargo(self):
        self.cargo 