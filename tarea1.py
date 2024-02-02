# Alfabeto
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
