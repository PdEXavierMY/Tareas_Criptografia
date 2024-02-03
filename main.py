from tarea1 import tarea1
from tarea2 import tarea2
from leer_qr import leer_codigo_qr

if __name__ == "__main__":
    eleccion = input("Elija el ejercicio a realizar (1/2): ")
    if eleccion == "1":
        texto = str(input("Ingrese el texto a descifrar: "))
        tarea1(texto)
    elif eleccion == "2":
        # Ruta de la imagen que contiene el código QR
        imagen_path = 'img/flag.png'
        # Obtener el contenido del código QR
        contenido_qr = leer_codigo_qr(imagen_path)[0]
        # Decodificar la cadena en base64
        tarea2(contenido_qr)
    else:
        print("Ejercicio no válido")