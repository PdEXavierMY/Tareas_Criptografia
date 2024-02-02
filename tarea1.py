letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cifrar_atbash(texto):
    texto = texto.lower()
    texto_cifrado = ""
    for letra in texto:
        if letra in letras:
            texto_cifrado += letras[-letras.index(letra)-1]
        else:
            texto_cifrado += letra
    return texto_cifrado