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
