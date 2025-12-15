class Controlador:
    def __init__(self):
        self.opcion1 = None
        self.opcion2 = None
        self.opcion3 = None

    def set_opcion(self, opcion):
        self.opcion1 = opcion

    def get_opcion(self):
        return self.opcion1

    def set_opcion2(self, opcion):
        self.opcion2 = opcion

    def get_opcion2(self):
        return self.opcion2

    def set_opcion3(self, opcion):
        self.opcion3 = opcion

    def get_opcion3(self):
        return self.opcion3