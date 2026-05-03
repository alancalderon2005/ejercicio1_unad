from Excepciones import errorreserva

class reserva:
    def __init__(self, cliente, servicio, duracion):
        if duracion <= 0:
            raise errorreserva("Duración Inválida")
        
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
    
    def confirmar(self):
        self.estado = "Confirmado"
    
    def cancelar(self):
        self.estado = "Cancelado"
    
    def calcular_total(self, impuesto=0, descuento=0):
        try:
            costo=self.servicio.calcular_costo(self.duracion)
        except Exception as e:
            raise errorreserva("Error calculando el costo") from e

        costo += costo*impuesto
        costo -= descuento
        return costo