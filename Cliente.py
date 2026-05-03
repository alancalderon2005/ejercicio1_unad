from Excepciones import ClienteInvalidoError, ClienteDuplicadoError

class Cliente:
    def __init__(self, nombre, email):
        self.__nombre = nombre
        self.__email = email
        self.validar()
    
    def validar(self):
        if not self.__nombre:
            raise ClienteInvalidoError("nombre", self.__nombre)
        if "@" not in self.__email:
            raise ClienteInvalidoError("email", self.__email)
    
    def get_nombre(self):
        return self.__nombre
    
    def get_email(self):
        return self.__email
    
    def __str__(self):
        return f"{self.__nombre} - {self.__email}"