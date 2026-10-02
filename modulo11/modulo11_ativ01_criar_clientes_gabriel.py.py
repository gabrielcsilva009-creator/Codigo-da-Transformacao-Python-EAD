import sqlite3

# Conectando ao banco de dados
conexao = sqlite3.connect("clientes.db")

# Criando o cursor para executar comandos SQL
cursor = conexao.cursor()

# Criando a tabela Clientes
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
""")

# Salvando as alterações
conexao.commit()

print("Tabela Clientes criada com sucesso!")

# Fechando a conexão
conexao.close()