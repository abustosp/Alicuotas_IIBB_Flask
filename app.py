from flask import Flask, render_template, request
import psycopg2
import json

app = Flask(__name__)

Credenciales = json.load(open('Credenciales.json'))

# Parámetros de conexión a la base de datos
dbname = Credenciales['dbname']
user = Credenciales['user']
password = Credenciales['password']
host = Credenciales['host']
port = Credenciales['port']

# Conexión a la base de datos con psycopg2
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        Provincia = request.form.getlist('Provincia')
        Codigo = request.form['Codigo']
        
        # Separar el codigo por comas, aplicar un trim y convertir a una tupla
        Codigo = tuple([i.strip() for i in Codigo.split(',')])
        
        # Transformar la lista de provincias en una tupla
        Provincia = tuple(Provincia)
        print(Provincia)

        # Check if Provincia list is not empty
        if Provincia:
            # Realizar la búsqueda en la base de datos
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM alicuotas_impuestos 
                           WHERE "Provincia" IN %s
                           AND "Codigo" IN %s''', 
                           ( 
                            Provincia, 
                            #Provincias_Hardcodeadas,
                            Codigo
                            ))
            resultados = cursor.fetchall()
            # Reemplazar los valores none por vacíos
            resultados = [list(i) for i in resultados]
            for i in resultados:
                for j in range(len(i)):
                    if i[j] == None:
                        i[j] = ''
            cursor.close()
                        
            return render_template('index.html', resultados=resultados)
        
    return render_template('index.html', resultados=None)


if __name__ == '__main__':
    app.run(debug=True)