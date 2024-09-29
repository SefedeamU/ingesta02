import pymysql
import csv
import boto3

# Conexión a la base de datos MySQL local
conexion = pymysql.connect(
    host='localhost',      # Usamos localhost porque MySQL está corriendo en la misma máquina
    user='root',           # Usuario de MySQL, en este caso root
    password='Mysql@123',  # La contraseña que configuraste para root
    database='mi_basededatos'  # El nombre de la base de datos que creamos
)

# Consulta a la tabla 'usuarios'
cursor = conexion.cursor()
cursor.execute("SELECT * FROM usuarios")
rows = cursor.fetchall()

# Guardar los resultados en un archivo CSV
ficheroUpload = "usuarios.csv"
with open(ficheroUpload, 'w', newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(['ID', 'Nombre', 'Apellido', 'Edad'])  # Encabezado
    escritor.writerows(rows)

print("Datos exportados a usuarios.csv")

# Subir el archivo CSV a S3
nombreBucket = "gcr-output-01"  # Reemplazar con el nombre de tu bucket
s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)

print(f"Archivo {ficheroUpload} subido a S3 en el bucket {nombreBucket}")
