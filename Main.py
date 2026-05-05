from Cliente import Cliente
from Servicio import ReservaSala, AlquilarEquipo, Asesorias
from Reserva import Reserva
from Excepciones import SistemaError
from Logger import registrar_log

def separador(titulo="\n"):
    if titulo:
        print(f"\n{titulo}")

def mostrar_cliente(cliente):
    print(f"[CLIENTE] Nombre: {cliente.get_nombre()} | Email: {cliente.get_email()}")

def mostrar_reserva(reserva):
    print(f"[RESERVA] Cliente: {reserva.cliente.get_nombre()} | Servicio: {reserva.servicio.nombre} | Duración: {reserva.estado}")

def sistema():
    
    clientes = []
    reservas = []
    
    #Agregar clientes simulados
    #1 Registro de cliente valido
    try:
        c1 = Cliente("Alan", "alan@mail.com")
        clientes.append(c1)
        separador("REGISTRO CLIENTE VÁLIDO")
        mostrar_cliente(c1)
    except SistemaError as e:
        print("Error:", e)
        return

    # 2 ERROR Registro de cliente invalido
    try:
        c2 = Cliente("Luis", "malcorreo")
        clientes.append(c2)
    except SistemaError as e:
        separador("REGISTRO CLIENTE INVÁLIDO")
        print("Error:", e)

    # 3 Creacion de servicios
    try:
        s1 = ReservaSala("Sala VIP", 50)
        s2 = AlquilarEquipo("Proyector", 30)
        s3 = Asesorias("Consultoría", 100)
        servicios = [s1,s2,s3]
        separador("CREACIÓN DE SERVICIOS")
        for s in servicios:
            print(f"[SERVICIO] {s.descripcion()}")
    except SistemaError as e:
        print("Error:", e)
        return

    # 4 Reserva exitosa con impuesto y descuento
    try:
        r1 = Reserva(c1, s1, 2) 
        reservas.append(r1)
        separador("RESERVA EXITOSA")
        mostrar_reserva(r1)
        r1.confirmar()
        print("Reserva confirmada")
        total = r1.calcular_total(0.19, 5) 
        print(f"Total: {total}")
    except SistemaError as e:
        print("Error:", e)

    # 5 ERROR Reserva con duracion invalida
    try:
        r2 = Reserva(c1, s2, -5) 
    except SistemaError as e:
        separador("ERROR RESERVA - DURACIÓN")
        print("Error:", e)
    
    # 6  Cancelar y confirmar reserva cancelada
    try:
        r3 = Reserva(c1, s3, 3) 
        reservas.append(r3)
        separador("CANCELAR Y ERROR AL CONFIRMAR")
        mostrar_reserva(r3)

        r3.cancelar()
        print("Reserva cancelada:")

        r3.confirmar() # ERROR
    except SistemaError as e:
        print("Error:", e)

    # 7 Reserva sin impuesto ni descuento
    try:
        r4 = Reserva(c1, s2, 1) 
        reservas.append(r4)
        separador("RESERVA SIN IMPUESTOS")
        mostrar_reserva(r4)

        total = r4.calcular_total()
        print("Total: {total}")
    except SistemaError as e:
        print("Error:", e)
        
    # 8 - Cliente valido  
    try:
        c3 = Cliente("Luis", "luis@mail.com")
        clientes.append(c3)
    except SistemaError as e:
        print("Error:", e)
        return
    else:
        separador("CLIENTE REGISTRADO")
        mostrar_cliente(c3)
        
    # 9 - Servicio con precio negativo 
    try:
        s4 = ReservaSala("Sala Invalida", -100)
        r5 = Reserva(c3, s4, 2)
        reservas.append(r5)
    except SistemaError as e:
        separador("SERVICIO INVÁLIDO")
        print("Error:", e)
    finally:
        print("Intento de reserva finalizado")
        
    # 10 - Registro de cliente duplicado  
    try:
        lista_emails = [c.get_email() for c in clientes]
        if "luis@mail.com" in lista_emails:
            raise SistemaError("El cliente luis@mail.com ya esta registrado")
        c4 = Cliente("Luis Copia", "luis@mail.com")
        clientes.append(c4)
    except SistemaError as e:
        separador("CLIENTE DUPLICADO")
        print("Error:", e)
    else:
        print("Cliente registrado:", c4)
    finally:
        print(f"\nTotal clientes registrados: {len(clientes)}")
        
if __name__ == "__main__":
    sistema()