------------- Sistema de Reservas - Manejo de Excepciones en Python-----------------

Proyecto colaborativo desarrollado para la **Fase 4** del curso de Programación (213023) de la Universidad Nacional Abierta y a Distancia (UNAD).

**Autores:** 
Luis Eduardo Guerrero Banda · Alan Joseph Calderón Farfán  
**Grupo:** 336


## Descripción

Sistema de gestión de reservas orientado a objetos que implementa un manejo robusto de excepciones en Python. El sistema permite registrar clientes, crear servicios y gestionar reservas, validando cada operación y registrando errores en un archivo de logs.

## Estructura del proyecto

```
main.py           # Punto de entrada y simulaciones del sistema
Cliente.py        # Clase Cliente con validaciones
Servicio.py       # Clases abstractas y concretas de servicios
Reserva.py        # Clase Reserva con estados y cálculo de costos
Excepciones.py    # Jerarquía de excepciones personalizadas
Logger.py         # Módulo de registro de eventos en archivo
logs.txt          # Archivo generado automáticamente con los logs
```
contiene 10 simulaciones de diferentes eventos para probar la ejecuacion del programa sin detenerse y registrando lo errores que puedan presentarse 

## Requisitos

- Python 3.8 o superior
- No requiere librerías externas

## Clonar el repositorio
bash

`git clone https://github.com/alancalderon2005/Proyecto_Software_FJ.git
cd Proyecto_Software_FJ
`

## Ejecución

```bash
python main.py
```

