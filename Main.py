from abc import ABC, abstractmethod

#Clases Madres
class empresa_fj(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass

class cliente:
    def __init__(self, nombre, email):
        self.__nombre = nombre
        self.__email = email
        self.validar()
    def validar(self):
        if "@" not in self.__email:
            raise ValueError ("\nEmail Inválido")

class servicio(ABC):
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base
    @abstractmethod
    def calcular_costo(self):
        pass

#Clases Hijas
class reserva_sala(servicio):
    def calcular_costo(self, horas):
        return self.precio_base * horas

class reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"