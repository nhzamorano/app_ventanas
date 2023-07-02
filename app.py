"""
Titulo: App desarrollada como corte uno para la Universiad Libre de Cali
Profesor: Diego Fernando Marin
Carrera: Ingenieria de sistemas
Materia: Programacion en python
Semestre: 2
Realizado por: Natanael Herrera
Descripcion: App diseñada para una empresa ficticia que permita la cotizar la fabricacion de ventanas, segun las
             dimensiones y los matertiales como vidrio y aluminio requeridos por el cliente.
Año: 2023-06-30 

Nota: Falta implementar estilos con css
"""

from flask import Flask, render_template, request, redirect, session 
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from cotizacion_ventanas import calcular
from crear_pdf import crearPDF
from utilidades import grabarCotizacion


cotizacion = ""
datos = ""
#Create the app
app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
    )
app.secret_key = 'ventanas'
#print(f'YOUR PASS: {generate_password_hash("sistemas")}')
dataBase = 'db/ventanas.db'
def crear_tablas():
    conexion = sqlite3.connect(dataBase)
    cursor = conexion.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user_name TEXT NOT NULL UNIQUE, password TEXT NOT NULL, full_name TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS precios_aluminio (id INTEGER PRIMARY KEY AUTOINCREMENT, type_al TEXT NOT NULL , cost INTEGER DEFAULT 0 NOT NULL)')
    cursor.execute('CREATE TABLE IF NOT EXISTS precios_vidrio (id INTEGER PRIMARY KEY AUTOINCREMENT, type_vid TEXT NOT NULL , cost REAL DEFAULT 0 NOT NULL)')
    cursor.execute('CREATE TABLE IF NOT EXISTS modelos_ventana (id INTEGER PRIMARY KEY AUTOINCREMENT, modelo TEXT NOT NULL , paneles INTEGER DEFAULT 1 NOT NULL, chapas INTEGER DEFAULT 0 NOT NULL)')

    cursor.execute('CREATE TABLE IF NOT EXISTS clients (nit INTEGER PRIMARY KEY NOT NULL UNIQUE, client_name TEXT NOT NULL UNIQUE, direccion TEXT NOT NULL, telefono1 TEXT NOT NULL, telefono2 TEXT, contacto TEXT NOT NULL)')

    cursor.execute('CREATE TABLE IF NOT EXISTS cotizaciones (id INTEGER PRIMARY KEY AUTOINCREMENT, id_client INTEGER, id_user INTEGER, modelo_ventana TEXT, tipo_aluminio TEXT, tipo_vidrio TEXT, creation_date TEXT, expiration_date TEXT, alto INTEGER, ancho INTEGER, cantidad_ventanas INTEGER, esmerilado INTEGER, costo_al REAL, costo_vid REAL, adicionales REAL, costo_paneles REAL, descuento REAL, iva REAL, total REAL, FOREIGN KEY (id_client) REFERENCES clients (nit), FOREIGN KEY (id_user) REFERENCES users (id) )')
    conexion.commit()
    conexion.close()
crear_tablas()

def modelos_ventana_list():
    modelos = []
    conexion = sqlite3.connect(dataBase)
    cursor = conexion.cursor()
    cursor.execute("SELECT modelo FROM modelos_ventana")
    result = cursor.fetchall()
    conexion.close()
    if result:
        modelos=result
    else:
        modelos=0
    return modelos

def tipos_aluminio():
    aluminio = []
    conexion = sqlite3.connect(dataBase)
    cursor = conexion.cursor()
    cursor.execute("SELECT type_al FROM precios_aluminio")
    result = cursor.fetchall()
    conexion.close()
    if result:
        aluminio=result
    else:
        aluminio=0
    return aluminio

def tipos_vidrio():
    vidrio = []
    conexion = sqlite3.connect(dataBase)
    cursor = conexion.cursor()
    cursor.execute("SELECT type_vid FROM precios_vidrio")
    result = cursor.fetchall()
    conexion.close()
    if result:
        vidrio=result
    else:
        vidrio=0
    return vidrio


@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('cotizar')
    return render_template('index.html')

@app.route('/administracion')
def administracion():
    return render_template('administracion.html')

@app.route('/aluminio', methods = ['GET','POST'])
def aluminio():
    if request.method == 'POST':
        tipo = request.form['tipo_aluminio']
        costo = request.form['costo']
        conexion = sqlite3.connect(dataBase)
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO precios_aluminio (type_al, cost) VALUES (?, ?)", (tipo, costo))
        conexion.commit()
        conexion.close()
        return redirect('administracion')
    return render_template('aluminio.html')

@app.route('/vidrio', methods=['GET','POST'])
def vidrio():
    if request.method == 'POST':
        tipo = request.form['tipo_vidrio']
        costo = request.form['costo']
        costo = float(costo.strip())
        conexion = sqlite3.connect(dataBase)
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO precios_vidrio (type_vid, cost) VALUES (?, ?)", (tipo, costo))
        conexion.commit()
        conexion.close()
        return redirect('administracion')

    return render_template('vidrio.html') 

@app.route('/modelos_ventana', methods=['GET', 'POST'])
def modelos_ventana():
    if request.method == 'POST':
        modelo = request.form['modelo']
        modelo = modelo.strip()
        paneles = 1
        chapas = 0
        if modelo == 'XO':
            paneles = 2
            chapas = 1
        elif modelo == 'OXO':
            paneles = 3
            chapas = 1
        elif modelo == 'OXXO':
            paneles = 4
            chapas = 2
        conexion = sqlite3.connect(dataBase)
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO modelos_ventana (modelo, paneles, chapas) VALUES (?, ?, ?)", (modelo, paneles, chapas))
        conexion.commit()
        conexion.close()
        return redirect('administracion')
    
    return render_template('modelos_ventana.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect('cotizar')
    if request.method == 'POST':
        name = request.form['name']
        password = generate_password_hash(request.form['password'])
        full_name = request.form['full_name']
        conexion = sqlite3.connect(dataBase)
        cursor = conexion.cursor()
        cursor.execute('INSERT INTO users (user_name,password,full_name) VALUES (?, ?, ?)',(name,password,full_name))
        user_id = cursor.lastrowid 
        conexion.commit()
        conexion.close()
        session['user_id'] = user_id 
        return redirect('/cotizar')
    return render_template('register.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error=""
    if 'user_id' in session:
        return redirect('/cotizar')
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        conexion = sqlite3.connect(dataBase)
        cursor = conexion.cursor()
        cursor.execute('SELECT id,user_name,password FROM users WHERE user_name=?',(name,))
        result_rows = cursor.fetchall()
        conexion.close()
        
        if result_rows:
            pass_hash=result_rows[0][2]
            if check_password_hash(pass_hash,password):
                user_id=result_rows[0][0]
                session['user_id'] = user_id
                return redirect('/cotizar') 
            else:
                error = 'Password incorrecto, intente de nuevo'
        else:
            error='Usuario no existe, por favor registrese'
        return render_template('login.html', error=error)
    return render_template('login.html')
    
@app.route('/cotizar', methods = ['GET', 'POST'])
def cotizar():
    if 'user_id' not in session:
        return redirect('/')
    user_id=session['user_id']
    global datos
    global cotizacion
    if request.method == 'POST':
        modelo = request.form['modelo']
        acabado = request.form['tipo_aluminio']
        vidrio = request.form['tipo_vidrio']
        esmerilado = request.form['esmerilado']
        ancho = request.form['ancho']
        alto = request.form['alto']
        cantidad = request.form['cantidad']
        datos=(modelo,acabado,vidrio,esmerilado,int(ancho),int(alto),int(cantidad))
        cotizacion = calcular(datos)
        return render_template("cotizacion.html", datos=datos, cotizacion=cotizacion)
    modelos = modelos_ventana_list()
    aluminio = tipos_aluminio()
    vidrio = tipos_vidrio()

    return render_template('cotizar.html',modelos=modelos,aluminio=aluminio,vidrio=vidrio)

@app.route("/pdf",methods=["GET","POST"])
def pdf():
    if 'user_id' not in session:
        return redirect('/')
    user_id=session['user_id']
    global datos
    global cotizacion
    extras=(8001626528,user_id,'2023-07-01','2023-07-15')
    grabarCotizacion(extras,datos,cotizacion)
    crearPDF(datos,cotizacion)
    return render_template("pdf.html")

@app.route('/salir')
def salir():
    session.pop('user_id', None)
    return redirect('/')

if (__name__) == '__main__':
    app.run(debug=True)
