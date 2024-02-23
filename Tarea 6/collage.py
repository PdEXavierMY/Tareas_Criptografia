import cv2

# Cargar la imagen
image = cv2.imread('flag.jpg')

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar un umbral
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# Encontrar los contornos
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Crear un conjunto para almacenar las subimágenes únicas
subimages_set = set()

# Iterar sobre los contornos
for contour in contours:
    # Obtener las coordenadas y dimensiones del contorno
    x, y, w, h = cv2.boundingRect(contour)

    # Recortar la subimagen
    subimage = image[y:y+h, x:x+w]

    # Convertir la subimagen a una cadena de bytes para compararla con las subimágenes ya guardadas
    subimage_bytes = cv2.imencode('.jpg', subimage)[1].tobytes()

    # Agregar la subimagen al conjunto si no está repetida
    if subimage_bytes not in subimages_set:
        subimages_set.add(subimage_bytes)

        # Guardar la subimagen
        cv2.imwrite(f'subimage_{len(subimages_set)}.jpg', subimage)

# Mostrar la imagen original
cv2.imshow('Original', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
