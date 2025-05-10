import sqlite3

# Función para conectar a la base de datos
def conectar():
    conexion = sqlite3.connect('database.db')
    return conexion

# Función para crear la tabla de servicios
def crear_tabla_servicios():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS servicios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio TEXT,
            rating REAL,
            descripcion TEXT,
            imagen_url TEXT,
            maps_url TEXT,
            latitud REAL,
            longitud REAL,
            distancia_minutos INTEGER
        )
    ''')

    conexion.commit()
    conexion.close()

# Punto de entrada para ejecutar este script directamente
if __name__ == '__main__':
    crear_tabla_servicios()
    print('Tabla servicios creada correctamente.')
