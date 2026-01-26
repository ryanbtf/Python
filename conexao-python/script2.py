import psycopg2

conn = psycopg2.connect(
    database="meubanco",
    user="postgres",
    password="senha123",
    host="127.0.0.1",
    port="5432"
)

print("Conexão bem-sucedida!")

conn.close()