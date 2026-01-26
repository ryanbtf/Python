import psycopg2 as conector

# Abertura de conexão e aquisição de cursor
conexao = conector.connect(host='localhost', database='novadb', port='5432', user='postgres', password='1705')
cursor = conexao.cursor()

# Execução de um comando: SELECT... CREATE ...
comando = '''CREATE TABLE Pessoa (
                     cpf INTEGER NOT NULL,
                     nome TEXT NOT NULL,
                     nascimento DATE NOT NULL,
                     oculos BOOLEAN NOT NULL,
                     PRIMARY KEY (cpf)
                     );'''
 
cursor.execute(comando)
 
     # Efetivação do comando
conexao.commit()
cursor.close()
conexao.close()