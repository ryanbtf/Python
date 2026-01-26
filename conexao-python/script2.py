import psycopg2

try:
    # Estabelecendo a conexão
    conn = psycopg2.connect(
        database="nome_do_banco",
        user="seu_usuario",
        password="sua_password",
        host="127.0.0.1", # ou localhost
        port="5432"
    )
    print("Conexão bem-sucedida!")

    # Criando um cursor
    cur = conn.cursor()

    # Executando um comando
    cur.execute("SELECT version();")
    db_version = cur.fetchone()
    print(f"Versão do PostgreSQL: {db_version}")

    # Fechando cursor e conexão
    cur.close()
    conn.close()

except Exception as e:
    print(f"Erro ao conectar: {e}")