from tarea1 import tarea1
from tarea2 import tarea2
from leer_qr import leer_codigo_qr


def lanzador():
    eleccion = input(
        "Elija el ejercicio a realizar:\n1. Descifrar texto\n2. Decodificar código QR\n")
    if eleccion == "1":
        texto = str(input("Ingrese el texto a descifrar: "))
        tarea1(texto)
        lanzador()
    elif eleccion == "2":
        # Ruta de la imagen que contiene el código QR
        imagen_path = 'img/flag.png'
        # Obtener el contenido del código QR
        contenido_qr = leer_codigo_qr(imagen_path)[0]
        # Decodificar la cadena en base64
        tarea2(contenido_qr)
        lanzador()
    else:
        print("Ejercicio no válido")
