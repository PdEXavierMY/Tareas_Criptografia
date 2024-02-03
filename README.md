<h1 align="center">Tareas Criptografía</h1>

Pincha [aquí](https://github.com/PdEXavierMY/Tareas_Criptografia) para acceder al repositorio.

***

1. [Tarea 1: Descifra el mensaje oculto en la imagen](#tarea-1-descifra-el-mensaje-oculto-en-la-imagen)
2. [Tarea 2: Descifra el mensaje oculto del QR](#tarea-2-descifra-el-mensaje-oculto-del-QR)


<h2 align="center">Tarea 1: Descifra el mensaje oculto en la imagen</h2>

***

1. En criptografía, El cifrado por sustitución es un método de cifrado por el que  unidades de texto plano son sustituidas con texto cifrado siguiendo un sistema regular. 

2. Existe un tipo de cifrado denominado espejo. 

3. Este método es conocido como atbash. 

Atbash es un método muy común de cifrado (criptografía) del alfabeto hebreo. Pertenece a la llamada criptografía clásica y es un tipo de cifrado por sustitución. Se le denomina también método de espejo, pues consiste en sustituir la primera letra (álef) por la última (tav), la segunda (bet) por la penúltima (shin) y así sucesivamente. Uno de sus usos más célebres se da en el libro de Jeremías, donde a fin de no nombrar Babilonia ( ,לבב Babel) se utiliza el término, en atbashSesac ( ,ךשש Sheshakh). 

La tabla de sustitución de atbash para el alfabeto hebreo es la siguiente: 

Original נ מ ל כ י ט ח ז ו ה ד ג ב א ת ש ר ק צ פ ע ס 

Clave ח ט י כ ל מ נ ס ע פ צ ק ר ש ת א ב ג ד ה ו ז Una tabla de atbash para el alfabeto español sería así: 

Original  a b c d e f g h i j k l m n ñ o p q r s t u v w x y z 

Clave  Z Y X W V U T S R Q P O Ñ N M L K J I H G F E D C B A En todo caso, hay que tener presente que este método de cifrado se ideó para un abyad en el que solo se escriben las consonantes, que luego se vocalizan de manera más o menos arbitraria y, así, prácticamente cualquier palabra hebrea es pronunciable al cifrarse en atbash. En idiomas con escritura alfabética, como el español, es infrecuente que una palabra codificada en atbash sea pronunciable. 

Y el código correspondiente es:

```python
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Función para cifrar un texto con el cifrado atbash


def cifrar_atbash(texto):
    texto = texto.lower()
    texto_cifrado = ""
    for letra in texto:
        if letra in letras:
            texto_cifrado += letras[-letras.index(letra)-1]
        else:
            texto_cifrado += letra
    return texto_cifrado

# Función para descifrar un texto con el cifrado atbash


def descifrar_atbash(texto_cifrado):
    texto_cifrado = texto_cifrado.lower()
    texto_descifrado = ""
    for letra in texto_cifrado:
        if letra in letras:
            texto_descifrado += letras[-letras.index(letra)-1]
        else:
            texto_descifrado += letra
    return texto_descifrado

# Main para testear


if __name__ == "__main__":
    texto = str(input("Ingrese el texto a cifrar: "))
    print("Texto cifrado: ", cifrar_atbash(texto))
    texto_cifrado = str(input("Ingrese el texto a descifrar: "))
    print("Texto descifrado: ", descifrar_atbash(texto_cifrado))
```

Por lo tanto:

![image](https://github.com/PdEXavierMY/Tareas_Criptografia/assets/91721855/681d1350-1d90-4dd3-9b98-1d15535be874)

La solución es: theflagissaywearecrazy

El cifrado Atbash se fundamenta en el principio de recorrer el alfabeto y asignar a cada letra su contraparte ubicada al final de este. Desde una perspectiva matemática, se puede conceptualizar el alfabeto como una matriz, y aplicar la operación de intercambio mediante el uso de índices negativos opuestos. De esta manera, cada elemento del alfabeto se reemplaza por su opuesto simétrico, dando forma al proceso de cifrado Atbash.

En esencia:

![image](https://github.com/PdEXavierMY/Tareas_Criptografia/assets/91721855/712e1fb9-fe34-4a40-9a21-bbb88c7c52ff)

Donde i es la posición en el alfabeto de la letra correspondiente.

En python, por como funcionan los índices la fórmula quedaría adaptada a:

![image](https://github.com/PdEXavierMY/Tareas_Criptografia/assets/91721855/fdc1257f-49e0-4e12-8a15-7fb7e5d49778)

<h2 align="center">Tarea 2: Descifra el mensaje oculto del QR</h2>

***

Se ha implantado en la entrada de la universidad un sistema para entrar a clase mediante lectura de un código QR. Jose Antonio como persona responsable distribuye varios códigos QR para que los alumnos prueben sus teléfonos

¿Puedes leer el QR?

Pista:

1. Lee el código QR, con un lector o desde consola  

2. Para leer desde consola puedes utilizar zbar-tools  

3. Decodifica base64 muchas veces 

La mayoría de los lectores no leen bien el código debido a su tamaño por lo que puede hacerse la lectura vía command line utilizando zbarimg que viene incluido en el paquete 

Y el código correspondiente es:

```python
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
```
