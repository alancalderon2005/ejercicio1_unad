from Cliente import Cliente
from Servicio import ReservaSala, AlquilarEquipo, Asesorias
from Reserva import Reserva
from Excepciones import SistemaError
from Logger import registrar_log

def sistema():
    
    clientes = []
    reservas = []
    
    #Agregar clientes simulados
    #1
    try:
        c1 = Cliente("Alan", "alan@mail.com")
        clientes.append(c1)
        print("Cliente creado:", c1)
    except SistemaError as e:
        print("Error:", e)

    # 2 ERROR
    try:
        c2 = Cliente("", "malcorreo")
        clientes.append(c2)
    except SistemaError as e:
        print("Error:", e)

    # 3
    try:
        s1 = ReservaSala("Sala VIP", 50)
        s2 = AlquilarEquipo("Proyector", 30)
        s3 = Asesorias("Consultoría", 100)
        servicios = [s1,s2,s3]
        for s in servicios:
            print("Servicio:", s.descripcion())
    except SistemaError as e:
        print("Error:", e)

    # 4
    try:
        r1 = Reserva(c1, s1, 2)
        reservas.append(r1)
        print("Reserva creada:", r1)
        r1.confirmar()
        print("Reserva confirmada:", r1)
        total = r1.calcular_total(0.19, 5)
        print("Total reserva:", total)
    except SistemaError as e:
        print("Error:", e)

    # 5 ERROR
    try:
        r2 = Reserva(c1, s2, -5)
    except SistemaError as e:
        print("Error:", e)
    
    # 6
    try:
        r3 = Reserva(c1, s3, 3)
        reservas.append(r3)
        print("Reserva creada:", r3)

        r3.cancelar()
        print("Reserva cancelada:", r3)

        r3.confirmar()  # ERROR
    except SistemaError as e:
        print("Error:", e)

    # 7
    try:
        r4 = Reserva(c1, s2, 1)
        reservas.append(r4)
        print("Reserva creada:", r4)

        total = r4.calcular_total()
        print("Total reserva:", total)
    except SistemaError as e:
        print("Error:", e)

if __name__ == "__main__":
    sistema() 