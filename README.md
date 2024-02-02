<h1 align="center">Tareas Criptografía</h1>

Pincha [aquí](https://github.com/PdEXavierMY/Tareas_Criptografia) para acceder al repositorio.

***

1. [Tarea 1: Descifra el mensaje oculto en la imagen](#tarea-1-descifra-el-mensaje-oculto-en-la-imagen)


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

letras_Atbash(i) = letras_Alfabeto[-i]

En python, por como funcionan los índices la fórmula quedaría adaptada a:

letras_Atbash(i) = letras_Alfabeto[-(i+1)]
