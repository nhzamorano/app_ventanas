import sqlite3
#from base_datos import precios_aluminio, precios_vidrio, modelo_ventana

COSTO_X_ESQUINA = 4310
COSTO_CHAPA = 16200
COSTO_VIDRIO_ESMERILADO = 5.20
dataBase = 'db/ventanas.db'

modelos_ventana = ["O","XO","OXO","OXXO"]
aluminio = ["pulido","Lacado Brillante","Lacado Mate","Anodizado"]
vidrio_list = ["Transparente","Bronce", "Azul"]
esmerilado_lst = ["Si","No"]

def pedir_opciones(opciones):
    while True:
        for i, opcion in enumerate(opciones):
            print(f"{i}. {opcion}") 
        try:
            opc = int(input("Digite su opcion: "))
            if opc <=(len(opciones)) and opc >= 0:
                break
            else:
                    print("")
                    print("Digite una opcion valida del menu!!")
                    print("")
        except ValueError:
            print("")
            print("Digite una opcion valida del menu!!")
            print("")
    return opc  

"""def buscar_codigo(codigo, tabla):
    if tabla == "modelo_ventana":
        if codigo in modelo_ventana.keys():
            nombre = modelo_ventana[codigo]["nombre"]
    elif tabla == "precios_aluminio":
        if codigo in precios_aluminio.keys():
            nombre = precios_aluminio[codigo]["nombre"]
    elif tabla == "precios_vidrio":
        if codigo in precios_vidrio.keys():
            nombre = precios_vidrio[codigo]["nombre"]

    return nombre"""

def pedir_numeros(opcion):
    while True:
        try:
            opc = int(input(f"Digite {opcion}: "))
            if opc >= 0:
                break
            else:
                    print("")
                    print(f"Digite {opcion} valido!!")
                    print("")
        except ValueError:
            print("")
            print(f"Digite {opcion} valido!!")
            print("")
    return opc  

"""def pedir_datos():
    #1.	El programa debe pedir el estilo de la ventana
    print("Escoja el modelo de la ventana")
    cod_estilo_ventana = pedir_opciones(modelos_ventana)
    estilo = buscar_codigo(cod_estilo_ventana, "modelo_ventana")
    print()
    #2.	El programa debe pedir el tipo de acabado del aluminio
    print("Escoja el tipo de acabado del aluminio")
    cod_tipo_acabado_aluminio = pedir_opciones(aluminio)
    acabado = buscar_codigo(cod_tipo_acabado_aluminio, "precios_aluminio")
    print()
    #3.	El programa debe pedir el tipo de vidrio y si es esmerilado o no
    print("Escoja el tipo de vidrio")
    cod_tipo_vidrio = pedir_opciones(vidrio_list)
    vidrio = buscar_codigo(cod_tipo_vidrio, "precios_vidrio")
    print("Desea el vidrio esmerilado S=Si/N=No:")
    esm = pedir_opciones(esmerilado_lst)
    esmerilado = True if esm == 0 else False
    #4.	El programa debe pedir las dimensiones de la ventana
    ancho = pedir_numeros("el ancho de la ventana")
    alto = pedir_numeros("el alto de la ventana")
    #5.	El programa debe pedir la cantidad de ventanas a fabricar
    cantidad = pedir_numeros("la cantidad de ventanas")
    return estilo, acabado, vidrio, esmerilado, ancho, alto, cantidad"""

"""def buscar_datos(tipo,tabla):
    if tabla == "modelo_ventana":
        for codigo, nombre in modelo_ventana.items():
            if nombre["nombre"] == tipo:
                paneles = nombre["paneles"]
                chapas = nombre["chapas"]
                return paneles, chapas
    elif tabla == "precios_aluminio":
        for codigo, nombre in precios_aluminio.items():
            if nombre["nombre"] == tipo:
                costo = nombre["costo"]
                return costo
    elif tabla == "precios_vidrio":
        for codigo, nombre in precios_vidrio.items():
            if nombre["nombre"] == tipo:
                costo = nombre["costo"]
                return costo"""

def buscar_datos_modelo_ventana(modelo):
    paneles = 1
    conexion = sqlite3.connect(dataBase)
    cursor = conexion.cursor()
    #se le coloca , al final del valor comparativo para prevenir error de tupla
    cursor.execute("SELECT paneles FROM modelos_ventana WHERE modelo=?",(modelo,))
    result = cursor.fetchone()
    conexion.close()
    if result:
        paneles=result[0]
    else:
        paneles=0
    return paneles   

def buscar_datos_aluminio(tipo):
    aluminio = 0
    conexion = sqlite3.connect(dataBase)
    cursor = conexion.cursor()
    cursor.execute("SELECT cost FROM precios_aluminio WHERE type_al=?",(tipo,))
    result = cursor.fetchone()
    conexion.close()
    if result:
        aluminio=result[0]
    else:
        aluminio=0
    return aluminio

def buscar_datos_vidrio(tipo):
    vidrio = 0.0
    conexion = sqlite3.connect(dataBase)
    cursor = conexion.cursor()
    cursor.execute("SELECT cost FROM precios_vidrio WHERE type_vid=?",(tipo,))
    result = cursor.fetchone()
    conexion.close()
    if result:
        vidrio=result[0]
    else:
        vidrio=0
    return vidrio

def calcular_cantidades(alto,ancho,tipo_dato):
    """
    >>> calcular_cantidades((90,12,"aluminio"))
    (192)
    >>> calcular_cantidades((90,12,"vidrio"))
    (198)
    """
    if tipo_dato == "aluminio":
        cantidad = ((alto -3)*2) + ((ancho - 3)*2)
    elif tipo_dato == "vidrio":
        cantidad = ((alto -1.5)*2)+((ancho-1.5)*2)
    return cantidad

def calcular_costos_u(cant, valor,tipo_producto):
    if tipo_producto == "aluminio":
        valor = cant * valor
    elif tipo_producto == "vidrio":
        valor = cant * valor

    return valor

def calcular_costos_adicionales(costo_esmerilado, valor_chapas, valor_esquinas):
    costos_adicionales = costo_esmerilado + valor_chapas + valor_esquinas
    return costos_adicionales

def calcular_descuento(cantidad, sub_total, porcentaje):
    if cantidad >= 100:
        descuento = sub_total * (porcentaje/100)
    else:
        descuento = 0
    
    return descuento

def calcular(datos):
    """
    >>> calcular( ('O', 'pulido', 'transparente', False, 90, 12, 1) )
    (97344, 1633.5, 33440, 132417.5)
     >>> calcular( ('O', 'pulido', 'transparente', True, 90, 12, 1) )
    (97344, 1633.5, 33445.20, 132422.7)
    
    """
    estilo, acabado, vidrio, esmerilado, ancho, alto, cantidad = datos
    #modelo= buscar_datos(estilo,"modelo_ventana")
    modelo = buscar_datos_modelo_ventana(estilo)
    #print(f"Esmerilado: {esmerilado}")
    #paneles,chapas = modelo
    paneles = modelo
    #valor_aluminio = buscar_datos(acabado,"precios_aluminio")/100
    valor_aluminio = buscar_datos_aluminio(acabado)/100
    #valor_vidrio = buscar_datos(vidrio,"precios_vidrio")
    valor_vidrio = buscar_datos_vidrio(vidrio)
    #6.	El programa debe calcular la cantidad de aluminio, la cantidad de vidrio requerido 
    # para fabricar la ventana
    cantidad_aluminio = calcular_cantidades(alto,ancho,"aluminio")
    cantidad_vidrio = calcular_cantidades(alto,ancho,"vidrio")
    #7.	El programa de calcular el costo del vidrio, el costo del aluminio, el costo de las esquinas 
    #y el costo de las chapas según la cantidad
    costo_aluminio = calcular_costos_u(cantidad_aluminio, valor_aluminio, "aluminio")
    costo_vidrio = calcular_costos_u(cantidad_vidrio, valor_vidrio, "vidrio")
    costo_esmerilado = COSTO_VIDRIO_ESMERILADO  if esmerilado=="si" else 0
    valor_chapas = COSTO_CHAPA * 2 if estilo == "OXXO" else  COSTO_CHAPA
    valor_esquinas = COSTO_X_ESQUINA * 4
    costos_adicionales = calcular_costos_adicionales(costo_esmerilado, valor_chapas, valor_esquinas)

    #Subtotal por panel o nave
    costo_x_panel = costo_aluminio + costo_vidrio + costos_adicionales
    #Costo total panles * cantidad de ventanas
    total_costo_panles = costo_x_panel * paneles 
    sub_total = total_costo_panles * cantidad

    iva = sub_total * 0.19 
    descuento = calcular_descuento(cantidad, sub_total, 10)
    #8.	El programa debe calcular el costo de fabricación de la ventana 
    costo_total = sub_total - descuento + iva
    return paneles, costo_aluminio, costo_vidrio, costos_adicionales, costo_x_panel, total_costo_panles, sub_total, descuento, iva, costo_total


"""
9.	El programa debe mostrar la cotización con los costos de fabricación  de la ventana
"""
def mostrar_datos(datos, cotizacion):
    estilo, acabado, vidrio, esmerilado, ancho, alto, cantidad = datos
    paneles, costo_aluminio, costo_vidrio, costos_adicionales, costo_x_panel, total_costo_panles, sub_total, descuento, iva, costo_total = cotizacion
    acabado_vidrio = " Esmerilado " if esmerilado == True else "Sin esmerilar"
    print()
    print("COMPAÑIA PQR")
    print("Fabricacion de Ventanas")
    print("Cotizacion")
    print()
    print(f"Modelo de la ventana: {estilo} cantindad de naves: {paneles}")
    print(f"Aluminio tipo de acabado: {acabado}")
    print(f"Tipo de vidrio: {vidrio} {acabado_vidrio}")
    print(f"Ventana {ancho} cm de ancho por {alto} cm de alto")
    print(f"+Costo Aluminio: {costo_aluminio:60.2f}")
    print(f"+Costo vidrio: {costo_vidrio:62.2f}")
    print(f"+Costos adicionales (Esmerilado, Esquinas, chapas) {costos_adicionales:26.2f}")
    print(f"Total costo panel {costo_x_panel:59.2f}")
    print(f"*Numero paneles por ventana {paneles:45}")
    print(f"=Costo de los {paneles} panel(es) de la ventana: {total_costo_panles:36.2f}")
    print(f"*Cantidad de ventanas: {cantidad:50}")
    print(f"Sub total: {sub_total:66.2f}")
    print(f"-Descuento 10%: {descuento:61.2f}")
    print(f"+IVA 19% {iva:68.2f}")
    print(f"Total Ventanas: {costo_total:61.2f}")
    #print(f"Producto: {nombre_producto.upper():20} cantidad: {cantidad:2} valor unitario: ${costo_unitario:10.2f} total x producto: ${valorxProducto:10.2f}")



"""def principal():
    datos = pedir_datos()
    print(datos)
    cotizacion = calcular(datos)
    mostrar_datos(datos, cotizacion)
"""
"""if __name__ == "__main__":
    import doctest
    doctest.testmod()    
"""
#principal()
