from datetime import datetime

def registrar_log(mensaje, nivel="Error"):
    try:
        with open("logs.txt", "a", encoding="utf-8") as f:
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{fecha}] {nivel}: {mensaje}\n")
    except Exception as e:
        print("Error escribiendo log: ", e)