from fpdf import FPDF
import os

#Crear un objeto PDF
pdf = FPDF(orientation="portrait",unit="mm", format="Letter")
ancho = 215.9
alto = 279.4
margen = 5

def cuadricula(col=(0,0,0), sep=10):
    pdf.set_draw_color(*col)
    for x in range(0, int(ancho), sep):
        pdf.line(x,0,x,alto)
    for y in range(0, int(ancho), sep):
        pdf.line(0,y,ancho,y)
    pdf.set_draw_color(0)

def formatear_num(v):
    valor = '{:,.2f}'.format(v)
    return valor

def crearPDF(datos,cotizacion):
    modelo,aluminio,vidrio,esm,anchov,altov,cantidad = datos
    paneles,costo_al,costo_vi,costos_ad, costo_un_paneles,costo_tot_paneles,sub_total,descuento,iva,total  = cotizacion

    if esm == 'si':
        vidrio = vidrio + " Esmerilado"
    elif esm == 'no':
        vidrio = vidrio + " Sin esmerilar"

    pdfs = os.listdir("static/pdf/")
    if pdfs !=[]:
        #Ojo si esta aberto no lo borra, hay que capturar ese error y enviarlo al usuario
        os.remove("static/pdf/cotizacion.pdf")
    #Una pagina y la cuadricula
    pdf.add_page()
    """cuadricula((255,216,216),5)
    cuadricula((188,188,255),10)
    cuadricula((188,255,188),20)"""

    #Cabecera
    pdf.set_xy(margen, margen)
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_xy(margen+10, margen-2)
    pdf.set_text_color(0,199,113)
    pdf.cell(w=ancho-2*margen, h=15.0, align="C", txt="COMPAÑIA PQR")
    pdf.set_xy(margen+10,margen+3)
    pdf.cell(w=ancho-2*margen,h=15.0,align="C",txt="Fabricacion de Ventanas")
    """pdf.set_xy(margen+10,margen+9)
    pdf.cell(w=ancho-2*margen,h=15.0,align="C",txt="COTIZACION")
    """
    #Zona izquierda Diereccion empresa
    pdf.set_font("Helvetica","",10)
    pdf.set_xy(margen-1, margen+20)
    pdf.set_text_color(0,0,0)
    pdf.cell(w=ancho-2*margen, h=15.0, align="L",txt="Ciudad     ")
    pdf.set_xy(margen+19, margen+20)
    pdf.cell(w=ancho-2*margen, h=15.0, align="L",txt="Santiado de Cali")

    pdf.set_xy(margen-1, margen+25)
    pdf.cell(w=ancho-2*margen, h=15.0, align="L",txt="Direccion ")
    pdf.set_xy(margen+19, margen+25)
    pdf.cell(w=ancho-2*margen, h=15.0, align="L",txt="Avenidad 6N No. 18N - 35")

    pdf.set_xy(margen-1, margen+30)
    pdf.cell(w=ancho-2*margen, h=15.0, align="L",txt="Telefonos ")
    pdf.set_xy(margen+19, margen+30)
    pdf.cell(w=ancho-2*margen, h=15.0, align="L",txt="2 680 44 16")

    pdf.set_xy(margen-1, margen+35)
    pdf.cell(w=ancho-2*margen, h=15.0, align="L",txt="Asesor     ")
    pdf.set_xy(margen+19, margen+35)
    pdf.cell(w=ancho-2*margen, h=15.0, align="L",txt="Pedro Picapiedra")

    pdf.set_xy(margen-1, margen+40)
    pdf.cell(w=ancho-2*margen, h=15.0, align="L",txt="E-mail      ")
    pdf.set_xy(margen+19, margen+40)
    pdf.cell(w=ancho-2*margen, h=15.0, align="L",txt="ppicapiedra@companiapqr.com")

    pdf.set_xy(margen-1, margen+45)
    pdf.cell(w=ancho-2*margen, h=15.0, align="L",txt="Sitio Web ")
    pdf.set_xy(margen+19, margen+45)
    pdf.cell(w=ancho-2*margen, h=15.0, align="L",txt="www.companiapqr.com.co")

    #Zona izquierda
    pdf.set_xy(margen+154, margen+20)
    pdf.cell(w=ancho-2*margen, h=15.0, align="L", txt="Fecha ")
    pdf.set_xy(margen+179, margen+20)
    pdf.cell(w=ancho-2*margen, h=15.0, align="L", txt="Jun/28/2023")

    pdf.set_xy(margen+154, margen+25)
    pdf.cell(w=ancho-2*margen, h=15.0, align="L", txt="Cotizacion No. ")
    pdf.set_xy(margen+179, margen+25)
    pdf.cell(w=ancho-2*margen, h=15.0, align="L", txt="1904362")

    pdf.set_xy(margen+154, margen+30)
    pdf.cell(w=ancho-2*margen, h=15.0, align="L", txt="Cliente ID ")
    pdf.set_xy(margen+179, margen+30)
    pdf.cell(w=ancho-2*margen, h=15.0, align="L", txt="A1")

    pdf.set_xy(margen+154, margen+35)
    pdf.cell(w=ancho-2*margen, h=15.0, align="L", txt="Vencimiento  ")
    pdf.set_xy(margen+179, margen+35)
    pdf.cell(w=ancho-2*margen, h=15.0, align="L", txt="Jul/02/2023")

    #Cliente
    fill=True 
    pdf.set_xy(margen, margen+60)
    pdf.set_fill_color(10, 200, 113)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(w=65, h=5, align="L", txt="CLIENTE", fill=True)
    pdf.rect(margen,margen+60,65,5)
    
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(margen, margen+70)
    pdf.cell(w=70, h=5,align="L", txt="Nombre ")
    pdf.set_xy(margen+20, margen+70)
    pdf.cell(w=70, h=5,align="L", txt="CONSTRUCTORA MARMOL Y CIA")

    pdf.set_xy(margen, margen+75)
    pdf.cell(w=70, h=5,align="L", txt="Contacto ")
    pdf.set_xy(margen+20, margen+75)
    pdf.cell(w=70, h=5,align="L", txt="Pablo Marmol")

    pdf.set_xy(margen, margen+80)
    pdf.cell(w=70, h=5,align="L", txt="Direccion ")
    pdf.set_xy(margen+20, margen+80)
    pdf.cell(w=70, h=5,align="L", txt="Avenida 5 No. 66 - 27")

    pdf.set_xy(margen, margen+85)
    pdf.cell(w=70, h=5,align="L", txt="Ciudad ")
    pdf.set_xy(margen+20, margen+85)
    pdf.cell(w=70, h=5,align="L", txt="Cali - Valle")

    pdf.set_xy(margen, margen+90)
    pdf.cell(w=70, h=5,align="L", txt="Telefonos ")
    pdf.set_xy(margen+20, margen+90)
    pdf.cell(w=70, h=5,align="L", txt="340 826 36 98 - 316 443 23 89")

    #Cuerpo de la cotizacon
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(0,199,113)
    pdf.set_xy(margen+10,margen+95)
    pdf.cell(w=ancho-2*margen,h=15.0,align="C",txt="COTIZACION")
    
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(0,0,)
    pdf.set_xy(margen+85,margen+100)
    pdf.cell(w=ancho-2*margen,h=15.0,align="L",txt="Modelo Ventana")
    pdf.set_xy(margen+125,margen+100)
    pdf.cell(w=ancho-2*margen,h=15.0,align="L",txt=modelo)

    pdf.set_xy(margen+85,margen+105)
    pdf.cell(w=ancho-2*margen,h=15.0,align="L",txt="Tipo Aluminio")
    pdf.set_xy(margen+125,margen+105)
    pdf.cell(w=ancho-2*margen,h=15.0,align="L",txt=aluminio)

    pdf.set_xy(margen+85,margen+110)
    pdf.cell(w=ancho-2*margen,h=15.0,align="L",txt="Tipo Vidrio")
    pdf.set_xy(margen+125,margen+110)
    pdf.cell(w=ancho-2*margen,h=15.0,align="L",txt=vidrio)

    pdf.set_xy(margen+85,margen+115)
    pdf.cell(w=ancho-2*margen,h=15.0,align="L",txt="Dimensiones Ventana ")
    pdf.set_xy(margen+125,margen+115)
    pdf.cell(w=ancho-2*margen,h=15.0,align="L",txt=str(anchov) + " cm de ancho por " + str(altov) + " cm de alto")

    pdf.set_xy(margen+75, margen+130)
    pdf.set_fill_color(10, 200, 113)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(w=85, h=5, align="C",txt="DETALLE", fill=True)
    pdf.set_xy(margen+145, margen+130)
    pdf.cell(w=45, h=5, align="C",txt="VALOR", fill=True)

   
    pdf.set_xy(margen+75, margen+135)
    pdf.set_text_color(0,0,0)
    pdf.cell(w=85, h=5, align="L",txt="Costo del Aluminio")
    pdf.set_xy(margen+145, margen+135)
    pdf.cell(w=45, h=5, align="R",txt=str(formatear_num(costo_al)))

    pdf.set_xy(margen+75, margen+140)
    pdf.cell(w=85, h=5, align="L",txt="Costo del Vidrio")
    pdf.set_xy(margen+145, margen+140)
    pdf.cell(w=45, h=5, align="R",txt=str(formatear_num(costo_vi)))

    pdf.set_xy(margen+75, margen+145)
    pdf.cell(w=85, h=5, align="L",txt="Costos adicionales (Esmerilado, Esquinas, Chapas)")
    pdf.set_xy(margen+145, margen+145)
    pdf.cell(w=45, h=5, align="R",txt=str(formatear_num(costos_ad)))

    pdf.set_xy(margen+75, margen+150)
    pdf.cell(w=85, h=5, align="L",txt="Total costo por panel")
    pdf.set_xy(margen+145, margen+150)
    pdf.cell(w=45, h=5, align="R",txt=str(formatear_num(costo_un_paneles)))

    pdf.set_xy(margen+75, margen+155)
    pdf.cell(w=85, h=5, align="L",txt="Numero de paneles por ventana")
    pdf.set_xy(margen+145, margen+155)
    pdf.cell(w=45, h=5, align="R",txt=str(paneles))

    pdf.set_xy(margen+75, margen+160)
    pdf.cell(w=85, h=5, align="L",txt=f"Costo de los {paneles} panel(es) de la ventana")
    pdf.set_xy(margen+145, margen+160)
    pdf.cell(w=45, h=5, align="R",txt=str(formatear_num(costo_tot_paneles)))

    pdf.set_xy(margen+75, margen+165)
    pdf.cell(w=85, h=5, align="L",txt="Cantidad de ventanas")
    pdf.set_xy(margen+145, margen+165)
    pdf.cell(w=45, h=5, align="R",txt=str(cantidad))

    pdf.set_xy(margen+75, margen+170)
    pdf.cell(w=85, h=5, align="L",txt="Sub-Total")
    pdf.set_xy(margen+145, margen+170)
    pdf.cell(w=45, h=5, align="R",txt=str(formatear_num(sub_total)))

    pdf.set_xy(margen+75, margen+175)
    pdf.cell(w=85, h=5, align="L",txt="Descuento")
    pdf.set_xy(margen+145, margen+175)
    pdf.cell(w=45, h=5, align="R",txt=str(formatear_num(descuento)))

    pdf.set_xy(margen+75, margen+180)
    pdf.cell(w=85, h=5, align="L",txt="IVA")
    pdf.set_xy(margen+145, margen+180)
    pdf.cell(w=45, h=5, align="R",txt=str(formatear_num(iva)))  

    pdf.set_xy(margen+75, margen+185)
    pdf.cell(w=85, h=5, align="L",txt=f"Costo total de la(s) {cantidad} ventana(s)")
    pdf.set_xy(margen+145, margen+185)
    pdf.cell(w=45, h=5, align="R",txt=str(formatear_num(total)))

    #Terminos y condiciones
    pdf.set_xy(margen+70,margen+195)
    pdf.set_fill_color(10, 200, 113)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(w=125, h=5, align="C", txt="TERMINOS Y CONDICIONES", fill=True)

    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(margen+70,margen+200)
    pdf.cell(w=125,h=5,align="L",txt="1. Al cliente se le cobrarà despues de acepdada esta cotizaciòn")
    pdf.set_xy(margen+70,margen+205)
    pdf.cell(w=125,h=5,align="L",txt="2. El pago sera debitado antes de entregar los bienes y servicios")
    pdf.set_xy(margen+70,margen+210)
    pdf.cell(w=125,h=5,align="L",txt="3. Por favor enviar la cotizacion firmada al email indicado anteriormente")
    pdf.set_xy(margen+70,margen+215)
    pdf.cell(w=125,h=5,align="L",txt="La aceptacion del cliente (firmar a continuacion):")
    pdf.set_xy(margen+70,margen+225)
    pdf.cell(w=125,h=5,align="L",txt="Firma")
    #pdf.set_xy(margen+70,margen+230)
    pdf.line(margen+80,margen+230,margen+175,margen+230)
    pdf.set_xy(margen+70,margen+240)
    pdf.cell(w=125,h=5,align="C",txt="Cualquier duda con gusto sera aclarada")


    pdf.output("static/pdf/cotizacion.pdf")

#En otra variable enviar los datos de la compañia y del cliente
"""datos=('OXXO','Lacado Brillante','Azul','no',12,90,101)
cotizacion=(4, 104064.0, 2524.5, 49645.2, 156233.7, 624934.8, 63118414.800000004, 6311841.48, 11992498.812, 68799072.13200001)
crearPDF(datos,cotizacion)"""