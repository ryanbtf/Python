import psycopg

conn = psycopg.connect(
    database="meubanco",
    user="postgres",
    password="senha123",
    host="localhost",
    port="5432"
)

print("Conexao bem-sucedida!")

conn.close()