import sqlite3

dataBase = 'db/ventanas.db'
def grabarCotizacion(extras,datos,cotizacion):
    id_cliente, id_user,fecha,fecha_exp = extras
    modelo_ventana, tipo_aluminio, tipo_vidrio,esmerilado,ancho,alto,cantidad = datos
    esm = 1  if esmerilado=="si" else 0
    paneles,costo_al,costo_vi,costos_ad, costo_un_paneles,costo_tot_paneles,sub_total,descuento,iva,total  = cotizacion
    conexion = sqlite3.connect(dataBase)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO cotizaciones (id_client, id_user,modelo_ventana,tipo_aluminio,tipo_vidrio,creation_date,expiration_date,alto,ancho,cantidad_ventanas,esmerilado,costo_al,costo_vid,adicionales,costo_paneles,descuento,iva,total) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id_cliente, id_user,modelo_ventana,tipo_aluminio,tipo_vidrio,fecha,fecha_exp,alto,ancho,cantidad,esm,costo_al,costo_vi,costos_ad,costo_un_paneles,descuento,iva,total))
    conexion.commit()
    conexion.close()



"""extras=(8001626528,1,'2023-07-01','2023-07-15')
datos=('OXXO','Lacado Brillante','Azul','no',12,90,101)
cotizacion=(4, 104064.0, 2524.5, 49645.2, 156233.7, 624934.8, 63118414.800000004, 6311841.48, 11992498.812, 68799072.13200001)
grabarCotizacion(extras,datos,cotizacion)"""