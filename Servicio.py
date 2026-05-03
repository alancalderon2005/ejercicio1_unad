from abc import ABC, abstractmethod
from Excepciones import errorservicio

class servicio(ABC):
    def __init__(self, nombre, precio_base):
        if precio_base <= 0:
            raise errorservicio("Precio Inválido")
        self.nombre = nombre
        self.precio_base = precio_base
    
    @abstractmethod
    def calcular_costo(self, tiempo):
        pass

class reservasala(servicio):
    def calcular_costo(self, horas):
        return self.precio_base * horas

class alquilarequipo(servicio):
    def calcular_costo(self, dias):
        return self.precio_base * dias

class asesorias(servicio):
    def calcular_costo(self, horas):
        return self.precio_base * horas * 1.2