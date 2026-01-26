import psycopg2

conn = psycopg2.connect(
    database="meubanco",
    user="postgres",
    password="senha123",
    host="localhost",
    port="5432"
)

print("Conexão bem-sucedida!")

conn.close()