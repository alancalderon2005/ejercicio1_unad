from abc import ABC, abstractmethod
from Excepciones import ServicioInvalidoError

class Servicio(ABC):
    def __init__(self, nombre, precio_base):
        if precio_base <= 0:
            raise ServicioInvalidoError(nombre, "Precio debe ser mayor a 0")
        self.nombre = nombre
        self.precio_base = precio_base
    
    @abstractmethod
    def calcular_costo(self, tiempo):
        pass
    @abstractmethod
    def descripcion(self):
        pass

class ReservaSala(Servicio):
    def calcular_costo(self, horas):
        return self.precio_base * horas
    def descripcion(self):
        return "Reserva de sala por horas"

class AlquilarEquipo(Servicio):
    def calcular_costo(self, dias):
        return self.precio_base * dias
    def descripcion(self):
        return "Alquiler de equipos por días"

class Asesorias(Servicio):
    def calcular_costo(self, horas):
        return self.precio_base * horas * 1.2
    def descripcion(self):
        return "Asesoria especializada"