import pymysql
import csv
import boto3

# Conexión a la base de datos MySQL
conexion = pymysql.connect(
    host='localhost',
    user='root',  # Asegúrate de que el usuario sea correcto
    password='Mysql@123',  # Reemplaza con la contraseña de MySQL si es necesaria
    database='mi_basededatos'
)

# Consulta a la tabla 'usuarios'
cursor = conexion.cursor()
cursor.execute("SELECT * FROM usuarios")
rows = cursor.fetchall()

# Guardar los resultados en un archivo CSV
ficheroUpload = "resultado_final.csv"
with open(ficheroUpload, 'w', newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(['ID', 'Nombre', 'Apellido', 'Edad'])  # Encabezado
    escritor.writerows(rows)

print(f"Datos exportados a {ficheroUpload}")

# Subir el archivo CSV a S3
nombreBucket = "ingesta02-mysql"  # Asegúrate de que el bucket exista
s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)

print(f"Archivo {ficheroUpload} subido a S3 en el bucket {nombreBucket}")
