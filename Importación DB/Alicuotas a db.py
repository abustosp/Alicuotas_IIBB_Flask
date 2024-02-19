import pandas as pd
import json
import psycopg2
import sqlalchemy

# Nombre del archivo de Excel
Excel = "Alicuotas IIBB Onvio.xlsx"
df = pd.read_excel(Excel , sheet_name="IIBB")

# Lectura de las credenciales de la base de datos
Credenciales = json.load(open('Credenciales.json'))

# Parámetros de conexión a la base de datos

dbname = Credenciales['dbname']
user = Credenciales['user']
password = Credenciales['password']
host = Credenciales['host']
port = Credenciales['port']


# Conexión a la base de datos con SQLAlchemy
conn = sqlalchemy.create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')

# Lectura del archivo de Excel

df.to_sql('alicuotas_impuestos', conn, if_exists='replace', index=False)
