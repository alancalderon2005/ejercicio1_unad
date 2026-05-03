# Excepciones personalizadas del sistema Software FJ
# Clases base de excepciones del sistema 
# Base para todos los errores relacionados con reservas
class errorreserva(Exception):
    pass
 
# Base para todos los errores relacionados con clientes
class errorcliente(Exception):
    pass
 
# Base para todos los errores relacionados con servicios
class errorservicio(Exception):
    pass
 
#------ Excepciones especificas de cliente errorcliente------
# Se lanza cuando un campo del cliente tiene un valor invalido

class ClienteInvalidoError(errorcliente):
    def __init__(self, campo, valor):
        self.campo = campo
        self.valor = valor
        super().__init__(f"Dato invalido en el campo '{campo}': '{valor}'")
 
# Se lanza cuando se intenta registrar un cliente que ya existe
class ClienteDuplicadoError(errorcliente):
    def __init__(self, identificador):
        self.identificador = identificador
        super().__init__(f"El cliente '{identificador}' ya esta registrado")
 
# Se lanza cuando no se encuentra el cliente en el sistema
class ClienteNoEncontradoError(errorcliente):
    def __init__(self, identificador):
        self.identificador = identificador
        super().__init__(f"No se encontro el cliente '{identificador}'")
 
# Excepciones especificas de servicioe errorservicio
 
# Se lanza cuando un parametro del servicio esta fuera de rango 

class ServicioInvalidoError(errorservicio):
    def __init__(self, nombre, detalle):
        self.nombre = nombre
        self.detalle = detalle
        super().__init__(f"Parametro invalido en '{nombre}': {detalle}")
 
# Se lanza cuando el servicio no esta disponible en el momento
class ServicioNoDisponibleError(errorservicio):
    def __init__(self, nombre_servicio):
        self.nombre_servicio = nombre_servicio
        super().__init__(f"El servicio '{nombre_servicio}' no esta disponible")
 
# Se lanza cuando el servicio solicitado no existe en el sistema
class ServicioNoEncontradoError(errorservicio):
    def __init__(self, nombre_servicio):
        self.nombre_servicio = nombre_servicio
        super().__init__(f"No se encontro el servicio '{nombre_servicio}'")
 

# Excepciones especificas de reservaHeredan de errorreserva

# Se lanza cuando los datos de la reserva son incorrectos

class ReservaInvalidaError(errorreserva):
    def __init__(self, detalle):
        self.detalle = detalle
        super().__init__(f"Reserva invalida: {detalle}")
 
# Se lanza cuando la accion no corresponde al estado actual como confirmar una reserva ya confirmada
class EstadoReservaError(errorreserva):
    def __init__(self, id_reserva, estado_actual, accion):
        self.id_reserva = id_reserva
        self.estado_actual = estado_actual
        self.accion = accion
        super().__init__(
            f"No se puede '{accion}' la reserva '{id_reserva}' "
            f"porque su estado es '{estado_actual}'"
        )
 
# Se lanza cuando no se encuentra la reserva por su ID
class ReservaNoEncontradaError(errorreserva):
    def __init__(self, id_reserva):
        self.id_reserva = id_reserva
        super().__init__(f"No se encontro la reserva con ID '{id_reserva}'")
 
# Se lanza cuando el calculo del costo produce un resultado invalido
class CalculoCostoError(errorreserva):
    def __init__(self, detalle):
        self.detalle = detalle
        super().__init__(f"Error en el calculo del costo: {detalle}")
 