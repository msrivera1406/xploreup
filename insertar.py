import sqlite3

def conectar():
    conexion = sqlite3.connect('database.db')
    return conexion

def insertar_servicios():
    conexion = conectar()
    cursor = conexion.cursor()
    servicios = [
        {
            "nombre": "Rebel Wings Insurgentes Sur",
            "categoria": "Restaurante",
            "precio": "$$",
            "rating": 3.9,
            "descripcion": "Alitas y comida estadounidense en un ambiente casual.",
            "imagen_url": "static/images/Rebel wings.jpg",
            "maps_url": "https://maps.app.goo.gl/cq96wUiJs32kF3zz6",
            "latitud": 19.3748,
            "longitud": -99.1832,
            "distancia_minutos": 12
        },
        {
            "nombre": "Los Arcos Restaurant",
            "categoria": "Restaurante",
            "precio": "$$",
            "rating": 4.6,
            "descripcion": "Especialidad en mariscos y cocina mexicana.",
            "imagen_url": "static/images/Los Arcos.jpg",
            "maps_url": "https://maps.app.goo.gl/1t8yry4qpWMw54XM7",
            "latitud": 19.3711,
            "longitud": -99.17952,
            "distancia_minutos": 10
        },
        {
            "nombre": "Hospital San Ángel Inn Patriotismo",
            "categoria": "Salud",
            "precio": "$$$",
            "rating": 3.8,
            "descripcion": "Hospital privado que ofrece una amplia gama de especialidades médicas, servicios de diagnóstico y atención hospitalaria integral.",
            "imagen_url": "static/images/San Angel.jpg",
            "maps_url": "https://maps.app.goo.gl/EZrgJPNPQQSviLcj9",
            "latitud": 19.37633,
            "longitud": -99.18617,
            "distancia_minutos": 9
        },
        {
            "nombre": "BBVA Centro Pyme",
            "categoria": "Banco",
            "precio": "",
            "rating": 2.7,
            "descripcion": "Bancomer, cajero y ventanilla",
            "imagen_url": "static/images/BBVA.jpg",
            "maps_url": "https://maps.app.goo.gl/wNip3XNJiUXWvziZ9",
            "latitud": 19.37436417,
            "longitud": -99.17983058,
            "distancia_minutos": 7
        },
        {
            "nombre": "Banco Santander Suc. Parroquia",
            "categoria": "Banco",
            "precio": "",
            "rating": 3,
            "descripcion": "Santander, cajeros automáticos y ventanillas",
            "imagen_url": "static/images/Santander.jpeg",
            "maps_url": "https://maps.app.goo.gl/Q18H1RjTM9fUPPDHA",
            "latitud": 19.3721414,
            "longitud": -99.17864892,
            "distancia_minutos": 9
        },
        {
            "nombre": "HSBC Insurgentes",
            "categoria": "Banco",
            "precio": "",
            "rating": 2,
            "descripcion": "HSBC, cajeros automáticos y ventanillas",
            "imagen_url": "static/images/HSBC.jpg",
            "maps_url": "https://maps.app.goo.gl/45LgwZLu3ivKXaJo6",
            "latitud": 19.3714473,
            "longitud": -99.17944832,
            "distancia_minutos": 5
        },
        {
            "nombre": "Banco Multiva",
            "categoria": "Banco",
            "precio": "",
            "rating": 3.3,
            "descripcion": "Cajero automático",
            "imagen_url": "static/images/MULTIVA.jpg",
            "maps_url": "https://maps.app.goo.gl/WvqKKaU6gHpU9wxj9",
            "latitud": 19.37123052,
            "longitud": -99.18010936,
            "distancia_minutos": 7
        },
        {
            "nombre": "CI Banco Galerías Insurgentes",
            "categoria": "Banco",
            "precio": "",
            "rating": 4,
            "descripcion": "Cajero automático y ventanilla",
            "imagen_url": "static/images/CI Banco.png",
            "maps_url": "https://maps.app.goo.gl/7KUxhtpXbD5v95RP9",
            "latitud": 19.37102568,
            "longitud": -99.17832701,
            "distancia_minutos": 11
        },
        {
            "nombre": "Inbursa del Valle",
            "categoria": "Banco",
            "precio": "",
            "rating": 3.9,
            "descripcion": "Cajero automático y ventanilla grupo Inbursa",
            "imagen_url": "static/images/Inbursa.jpeg",
            "maps_url": "https://maps.app.goo.gl/7uELwtVe2hnoSDAD9",
            "latitud": 19.37495529,
            "longitud": -99.17832433,
            "distancia_minutos": 6
        },
        {
            "nombre": "Banamex Insurgentes",
            "categoria": "Banco",
            "precio": "",
            "rating": 5,
            "descripcion": "Cajero automático y ventanilla grupo Banamex",
            "imagen_url": "static/images/Banamex.jpg",
            "maps_url": "https://maps.app.goo.gl/3R4MEbw8z8FpHY3N7",
            "latitud": 19.37416121,
            "longitud": -99.17850118,
            "distancia_minutos": 6
        },
        {
            "nombre": "Especialista Dental",
            "categoria": "Salud",
            "precio": "$$",
            "rating": 5,
            "descripcion": "Clínica dental ubicada cerca del Centro Comercial Manacar, que ofrece servicios odontológicos generales y especializados.",
            "imagen_url": "static/images/Especialista Dental.jpg",
            "maps_url": "https://maps.app.goo.gl/FcNzdj4PPkocs8bq7",
            "latitud": 19.36976,
            "longitud": -99.18928,
            "distancia_minutos": 6
        }, 
        {
            "nombre": "Farmacia Integramed San Ángel Inn",
            "categoria": "Salud",
            "precio": "$$",
            "rating": 3,
            "descripcion": "Farmacia que ofrece medicamentos y productos para el cuidado de la salud.",
            "imagen_url": "static/images/Integramed.jpg",  # Llena este campo
            "maps_url": "https://maps.app.goo.gl/72W481CAaDPCDZQz5",
            "latitud": 19.37653873,
            "longitud": -99.18626743,
            "distancia_minutos": 3
        },
        {
            "nombre": "Farmacia Similares Félix Cuevas",
            "categoria": "Salud",
            "precio": "$$",
            "rating": 4.2,
            "descripcion": "Farmacia de cadena conocida por sus medicamentos genéricos y servicios de consulta médica a bajo costo.",
            "imagen_url": "static/images/Farmacias similares.jpg",  # Llena este campo
            "maps_url": "https://maps.app.goo.gl/T1s6jHyD4ufhYufD9",
            "latitud": 19.37347342,
            "longitud": -99.17646152,
            "distancia_minutos": 11
        },
        {
            "nombre": "Farmacias del Ahorro Suc. Juárez",
            "categoria": "Salud",
            "precio": "$$",
            "rating": 3.4,
            "descripcion": "Farmacia de cadena con una extensa variedad de medicamentos y servicios de salud.",
            "imagen_url": "static/images/Farmacias ahorro.jpg",  # Llena este campo
            "maps_url": "https://maps.app.goo.gl/VrfG8Dw2uqKU56fWA",
            "latitud": 19.37176549,
            "longitud": -99.18838682,
            "distancia_minutos": 4
        },
        {
            "nombre": "Farmacia Guadalajara Rev. San José",
            "categoria": "Salud",
            "precio": "$$",
            "rating": 3.8,
            "descripcion": "Farmacia Guadalajara, variedad de medicamentos y todo lo que busques.",
            "imagen_url": "static/images/Farmacias Guadalajara.jpg",  # Llena este campo
            "maps_url": "https://maps.app.goo.gl/9h7EAzdP7b43AMoz9",
            "latitud": 19.3703802,
            "longitud": -99.18789281,
            "distancia_minutos": 6
        },
        {
            "nombre": "Farmacias Benavides",
            "categoria": "Salud",
            "precio": "$$",
            "rating": 3.5,
            "descripcion": "Farmacia con un amplio catálogo de medicamentos y productos para el cuidado de la salud, que además ofrece servicio de consulta médica.",
            "imagen_url": "static/images/Farmacias Benavides.jpg",  # Llena este campo
            "maps_url": "https://maps.app.goo.gl/zH7JcmG297cvG6xf9",
            "latitud": 19.37376215,
            "longitud": -99.17739545,
            "distancia_minutos": 7
        },
        {
            "nombre": "Farmacia San Pablo Félix Cuevas",
            "categoria": "Salud",
            "precio": "$$",
            "rating": 3.2,
            "descripcion": "Farmacia de cadena que ofrece una amplia gama de medicamentos, productos para la salud y servicio de consulta médica.",
            "imagen_url": "static/images/Farmacias San Pablo.jpg",  # Llena este campo
            "maps_url": "https://maps.app.goo.gl/rtTBLsdTjRtBCDmq5",
            "latitud": 19.37376249,
            "longitud": -99.17603937,
            "distancia_minutos": 12
        },
        {
            "nombre": "Campomar Insurgentes",
            "categoria": "Restaurante",
            "precio": "$$$",
            "rating": 4.7,
            "descripcion": "Mariscos y cocina fusión en un ambiente moderno.",
            "imagen_url": "static/images/Campomar.jpg",  # Llena este campo
            "maps_url": "https://maps.app.goo.gl/o9qW1sEcD25wVsgG8",
            "latitud": 19.3718,
            "longitud": -99.17936,
            "distancia_minutos": 12
        }

    ]
    

    for servicio in servicios:
        cursor.execute('''
            INSERT INTO servicios (nombre, categoria, precio, rating, descripcion, imagen_url, maps_url, latitud, longitud, distancia_minutos)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            servicio["nombre"],
            servicio["categoria"],
            servicio["precio"],
            servicio["rating"],
            servicio["descripcion"],
            servicio["imagen_url"],
            servicio["maps_url"],
            servicio["latitud"],
            servicio["longitud"],
            servicio["distancia_minutos"]
        ))

    conexion.commit()
    conexion.close()
    print('Servicios insertados correctamente.')

if __name__ == '__main__':
    insertar_servicios()
