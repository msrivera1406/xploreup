from flask import Flask, render_template
from flask import Flask, render_template, send_from_directory
import sqlite3

app = Flask(__name__)

def obtener_servicios():
    conexion = sqlite3.connect('database.db')
    conexion.row_factory = sqlite3.Row  # Para que podamos acceder a las columnas por nombre
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM servicios ORDER BY RANDOM()')
    servicios = cursor.fetchall()
    conexion.close()
    return servicios
def obtener_mejores_Servicios(): 
    conexion = sqlite3.connect('database.db')
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()

    cursor.execute('SELECT DISTINCT categoria FROM servicios')
    categorias = [fila['categoria'] for fila in cursor.fetchall()]

    servicios_filtrados = []

    for categoria in categorias:
        cursor.execute('''
            SELECT * FROM servicios
            WHERE categoria = ? AND rating >= 4
            ORDER BY rating DESC
            LIMIT 5
        ''', (categoria,))
        
        servicios_categoria = cursor.fetchall()
        
        for servicio in servicios_categoria:
            servicios_filtrados.append(dict(servicio))

    conexion.close()
    return servicios_filtrados
def obtener_servicios_random(limit=15):
    conexion = sqlite3.connect('database.db')
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    cursor.execute(f'SELECT * FROM servicios ORDER BY RANDOM() LIMIT {limit}')
    servicios = cursor.fetchall()
    conexion.close()
    return servicios

@app.route('/')
def index(): 
    servicios = obtener_servicios_random(limit=15)
    return render_template('index.html', servicios=servicios)

@app.route('/comida')
def comida():
    servicios=obtener_servicios()
    return render_template('comida.html', servicios=servicios)
@app.route('/super')
def super():
    servicios=obtener_servicios()
    return render_template('super.html', servicios=servicios)

@app.route('/papeleria')
def papeleria():
    servicios=obtener_servicios()
    return render_template('papeleria.html', servicios=servicios)

@app.route('/banco')
def banco():
    servicios=obtener_servicios()
    return render_template('banco.html', servicios=servicios)
@app.route('/salud')
def salud():
    servicios=obtener_servicios()
    return render_template('salud.html', servicios=servicios)

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('.', 'sitemap.xml')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)