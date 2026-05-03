def registrar_log(mensaje):
    try:
        with open("logs.txt", "a") as f:
            f.write(mensaje + "\n")
    except Exception as e:
        print("Error escribiendo log: ", e)