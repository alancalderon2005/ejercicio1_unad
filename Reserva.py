from Excepciones import (ReservaInvalidaError, EstadoReservaError, CalculoCostoError)

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        if duracion <= 0:
            raise ReservaInvalidaError("Duración Inválida")
        
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
    
    def confirmar(self):
        if self.estado !="Pendiente":
            raise EstadoReservaError("N/A", self.estado, "Confirmar")
        self.estado = "Confirmado"
    
    def cancelar(self):
        if self.estado == "Cancelado":
            raise EstadoReservaError("N/A", self.estado, "Cancelar")
        self.estado = "Cancelado"
    
    def calcular_total(self, impuesto=0, descuento=0):
        try:
            costo=self.servicio.calcular_costo(self.duracion)
        except Exception as e:
            raise CalculoCostoError("Error calculando el costo") from e

        costo += costo*impuesto
        costo -= descuento
        return costo
    
    def __str__(self):
        return f"Reserva ({self.estado}) - Cliente: {self.cliente.get_nombre()}"