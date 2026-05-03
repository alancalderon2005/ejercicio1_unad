from Excepciones import errorcliente

class cliente:
    def __init__(self, nombre, email):
        self.__nombre = nombre
        self.__email = email
        self.validar()
    
    def validar(self):
        if not self.__nombre:
            raise errorcliente("Nombre vacío")
        if "@" not in self.__email:
            raise errorcliente("Email inválido")
    
    def get_nombre(self):
        return self.__nombre
    
    def get_email(self):
        return self.__email