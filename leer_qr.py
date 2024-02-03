import cv2
from pyzbar.pyzbar import decode

# Función para leer un código QR desde una imagen y extraer su contenido
def leer_codigo_qr(imagen_path):
    # Cargar la imagen
    imagen = cv2.imread(imagen_path)
    
    # Convertir la imagen a escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Decodificar los códigos QR presentes en la imagen
    resultados = decode(imagen_gris)
    
    contenido_qr_list = []
    
    # Mostrar los resultados
    for resultado in resultados:
        # Extraer las coordenadas del rectángulo que rodea el código QR
        rectangulo = resultado.rect
        
        # Obtener las coordenadas del rectángulo
        x, y, w, h = rectangulo
        
        # Dibujar un rectángulo alrededor del código QR
        cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Obtener el contenido del código QR
        contenido_qr = resultado.data.decode('utf-8')
        
        contenido_qr_list.append(contenido_qr)
    
    # Mostrar la imagen con los rectángulos dibujados
    cv2.imshow('Imagen con código QR', imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return contenido_qr_list

''' Espacio de pruebas

# Ruta de la imagen que contiene el código QR
imagen_path = 'img/flag.png'

# Obtener el contenido del código QR
contenido_qr = leer_codigo_qr(imagen_path)

# Imprimir el contenido del código QR extraído
for contenido in contenido_qr:
    print("Contenido del código QR:", contenido)

'''