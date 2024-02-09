<h1 align="center">Tareas Criptografía</h1>

Pincha [aquí](https://github.com/PdEXavierMY/Tareas_Criptografia) para acceder al repositorio.

***

1. [Tarea 1: Descifra el mensaje oculto en la imagen](#tarea-1-descifra-el-mensaje-oculto-en-la-imagen)
2. [Tarea 2: Descifra el mensaje oculto del QR](#tarea-2-descifra-el-mensaje-oculto-del-QR)
3. [Tarea 3: Scrapping del correo](#tarea-3-scrapping-del-correo)


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
import base64


def decode_base64(cadena):
    return base64.b64decode(cadena).decode('utf-8')


# Cadena en base64 proporcionada
cadena_base64 = "Vm0wd2QyUXlWa2hWV0doVllteEtWMVl3WkRSWFJteFZVbTVrVmxKc2NIcFhhMk0xVmpGS2RHVkdXbFpOYm1oUVdWZDRTMk14VG5OWGJHUlRUVEZLVVZkV1kzaFRNVWw0V2toR1VtSlZXbFJXYWtwdlpWWmFkR05GU214U2JWSkpWbTEwYzJGV1NuUlZiR2hoVmpOb2FGWldXbUZqYkhCSlkwZDRVMkpXU2xsV1Z6QXhVekpHUjFOdVVtaFNlbXhXVm0weGIxSkdjRmRYYlhSWFRWWndlbFl5TVRSVk1rcFhVMnhzVjFaNlFYaFdSRXBIVWpGT2RWUnNhR2hsYlhoWlYxZDRiMVV3TUhoV1dHaFlZbGhTV0ZSV2FFTlRiR3QzV2tSU1ZrMUVSa1pXYlhCaFZqQXhkVlZ1V2xaaGExcGhXbFphVDJOdFNrZFRiV3hvWld4YWIxWnRNVEJXYXpGWFUydGtXRmRIYUZsWmEyaERZekZhYzFWclpGUmlSM2hYVmpKNGExWlhTa2RqUmxwWFlsaFNlbFpxUm1GU2JVVjZZVVprYUdFelFrbFdiWEJIVkRKU1YxZHVUbFJpVjNoVVZGY3hiMkl4V25STlJFWnJUVlZ3ZVZSV1ZtdGhiRXAwWVVoT1ZtRnJOVlJXTVZwaFkxWkdWVkpzVGs1WFJVcElWbXBLTkdFeFdsaFRiRnBxVWxkU1lWbFhjekZqYkZweFVtMUdVMkpWVmpaWlZWcHJWakZLVjJOSE9WaGhNVnBvVmtSS1RtVldUbkpoUjJoVFlrVndWVlp0TURGUk1rbDRWMWhvV0dKRk5WUlVWbFY0VGxaYWRFNVZPVmRpVlhCSVdUQmFjMWR0U2toaFJsSmFUVlp3VkZacVJuZFNWbEp5VGxkc1UySkhPVE5XYTFwaFZURlZlVkpyWkZoaWEzQndWV3RhZDFsV1duTlhibVJPVFZac00xWXlNVWRWTWtwR1RsUkdWazF1YUZoWlZWVjRZekZPY21KR2FGZFNXRUV5VjJ4V1lWbFdXWGhqUld4VllrWktjRlZxUmt0V1ZscEhWV3RLYTAxRVJsTlZSbEYzVUZFOVBRPT0="

# Decodificar la cadena en base64


def tarea2(mensaje):
    # Imprimir el resultado
    cadena_decodificada = decode_base64(mensaje)
    while True:
        print(cadena_decodificada)
        bool = input("¿Está la cadena decodificada? (S/N): ")
        if bool.lower() == "s":
            break
        else:
            cadena_decodificada = decode_base64(cadena_decodificada)


tarea2(cadena_base64)
```


Obteniendo como solución: flag{QR_puede_usarse_para_esconder_mensajes}

<h2 align="center">Tarea 3: Scrapping del correo electrónico</h2>

***

El código para extraer la matrícula es:

```python
from bs4 import BeautifulSoup

# HTML del correo electrónico
email_html = """
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  </head>
  <body bgcolor="#FFFFFF" text="#000000">
    <p>Buen dia, <br>
    </p>
    <p>Señor Donal le ruego acepte mis disculpas bajo ningun concepto
      era de mi intención faltarle al respeto.</p>
    <p>Le facilitaremos las hojas de reclamaciones y por las molestias
      ocasionadas le regalamos un lavado de coche, para cuando lo recoja
      lo tenga brillante .</p>
    <p>Saludos.<br>
    </p>
    <div id="gmail-m_-6342449059210445536Signature">
      <div id="gmail-m_-6342449059210445536divtagdefaultwrapper">
        <hr
style="width:320px;height:4px;border-width:0px;background-color:rgb(253,120,50);margin-left:0px">
        <p>Elustondo Raimundo</p>
        <p><font color="#fd7832">Director Estacionamiento Autorizado </font><br>
          Parking 133.</p>
      </div>
    </div>
    <div class="moz-cite-prefix">El 18/08/17 a las 06:33, Donal Furioso
      escribió:<br>
    </div>
    <blockquote type="cite"
cite="mid:CAEPjOfvX5AfyzE=i5fpL6gGjLF9gJgRwVT6Wa_AekcSf7nCTRQ@mail.gmail.com">
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
      <div dir="ltr">Elustondo, me parece una falta de respeto el
        intento de llevar al desguace mi automóvil, le voy a facilitar
        mis datos.
        <div><br>
        </div>
        <div>Matricula: C047057-R</div>
        <div>Fecha de matriculación: 24/02/1975</div>
        <div>Color: Azul Dignne</div>
        <div>Marca: SUSUKI</div>
        <div>Modelo:S5617</div>
        <div><br>
        </div>
        <div>Cuando recoja mi coche necesitaré que me faciliten una hoja
          de reclamaciones, por el accidente, los accesos de peatones
          están mal y el trato recibido no es el que debiera tras un
          accidente en sus instalaciones.</div>
        <div><br>
        </div>
        <div>Me despido sin saludo, ya que su persona no es de mi
          agrado.</div>
        <div><br>
        </div>
        <div>
          <div><b><font color="#073763">Donal Furioso</font></b><br>
            <blockquote type="cite" style="color:rgb(80,0,80)">
              <div dir="ltr"><br>
              </div>
            </blockquote>
            <div class="gmail_extra">
              <div class="gmail_quote">El 18 de agosto de 2017, 12:25,
                Estacionamiento Autorizado <span dir="ltr">&lt;<a
                    href="mailto:estacionamiento_autorizado133@outlook.es"
                    target="_blank" moz-do-not-send="true">estacionamiento_autorizado133@outlook.es</a>&gt;</span>
                escribió:<br>
                <blockquote class="gmail_quote" style="margin:0px 0px
                  0px 0.8ex;border-left:1px solid
                  rgb(204,204,204);padding-left:1ex">
                  <div bgcolor="#FFFFFF">
                    <p>Buenos días Mr.Furioso.</p>
                    <p>Para atender su consulta necesitamos que nos
                      facilite el número de matricula del automovil y la
                      fecha de matriculación , asi como el color , marca
                      y modelo del mismo. Sin todos estos datos no nos
                      es posible identificarlo y poder garantizar que es
                      suyo.</p>
                    <p>Si su amnesia se lo permite lo necesitamos a la
                      mayor brevedad, o al final de semana serán
                      retirados al desguace todos los coches en su misma
                      situación.</p>
                    <div id="gmail-m_-6342449059210445536Signature">
                      <div
                        id="gmail-m_-6342449059210445536divtagdefaultwrapper">
                        <hr
style="width:320px;height:4px;border-width:0px;background-color:rgb(253,120,50);margin-left:0px">
                        <p>Elustondo Raimundo</p>
                        <p><font color="#fd7832">Director
                            Estacionamiento Autorizado </font><br>
                          Parking 133.</p>
                      </div>
                    </div>
                    <br>
                    <div
                      class="gmail-m_-6342449059210445536moz-cite-prefix">El
                      18/08/17 a las 06:17, Donal Furioso escribió:<br>
                    </div>
                    <div>
                      <div class="gmail-h5">
                        <blockquote type="cite">
                          <div dir="ltr">Estimado director del parking
                            número 133.
                            <div><br>
                              <div>Hoy he tenido un percance a la salida
                                de la calle 133,🤒🤒 he sufrido una
                                amnesia por una brusca caída y no
                                recuerdo en que planta de su garaje he
                                dejado mi automóvil.<br>
                              </div>
                              <div><br>
                              </div>
                              <div>¿Podría ayudarme?😟</div>
                              <div><br>
                              </div>
                              <div>Saludos cordiales.</div>
                              <div><br>
                              </div>
                              <div><b><font color="#073763">Donal
                                    Furioso</font></b><br>
                              </div>
                            </div>
                          </div>
                        </blockquote>
                        <br>
                      </div>
                    </div>
                  </div>
                </blockquote>
              </div>
              <br>
            </div>
          </div>
        </div>
      </div>
    </blockquote>
    <br>
  </body>
</html>

"""
def tarea3(email_html):
    # Parsear el HTML
    soup = BeautifulSoup(email_html, 'html.parser')

    # Buscar la etiqueta que contiene la información de la matrícula
    etiqueta_matricula = soup.find(
        'div', text=lambda text: text and 'Matricula:' in text)

    # Si se encuentra la etiqueta, extraer la matrícula
    if etiqueta_matricula:
        matricula = etiqueta_matricula.text.split(': ')[1]
        print("Matrícula:", matricula)
    else:
        print("No se encontró la matrícula en el correo electrónico.")
```

Dando como solución: Matrícula: C047057-R

Y siendo su historia:


D.Furioso

MATRÍCULA = C047057-R
COLOR: AZUL DIGGNE
MARCA: SUSUKI
MODELO: S5617

HISTORIA DEL POBRE HOMBRE:

El 18/08/17 Donal Furioso sufrió una amnesia por una caída y se olvidó de en que planta del parking había dejado el coche aparcado. Por eso contacta con el director de este para solicitar ayuda. Al recibir una respuesta se entera de que debe al parking 23,76 y de que tiene que cambiar dos ruedas por vandalismo de las que el garaje no se hace responsable. Se da cuenta de que han intentado llevar al desguace su vehículo tras no proporcionar la información solicitada por el director a tiempo y acaba solicitando una hoja de reclamaciones por el accidente en el parking, los accesos a peatones en mal estado que causaron en cierta medida su caída y el mal trato que ha recibido en general. Al final de todo recibe un correo que estipula que debe al parking un total de 144.76 tras llevar su coche al desguace. Esta trágica historia finaliza con el director, Elustondo Raimundo, pidiendo disculpas por el trato recibido y regalandole al señor Furioso un lavado de coche gratis para que lo recoja brillante.

