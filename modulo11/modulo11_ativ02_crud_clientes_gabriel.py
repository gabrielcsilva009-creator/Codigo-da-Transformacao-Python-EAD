import sqlite3

# Conectando ao banco de dados
conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

# Criando a tabela caso ela ainda não exista
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
""")

# -------------------------
# INSERIR
# -------------------------

cursor.execute("""
    INSERT INTO Clientes (nome, email)
    VALUES (?, ?)
""", ("Gabriel", "gabriel@email.com"))

conexao.commit()

print("Cliente inserido com sucesso!")


# -------------------------
# CONSULTAR
# -------------------------

cursor.execute("SELECT * FROM Clientes")

clientes = cursor.fetchall()

print("\nClientes cadastrados:")

for cliente in clientes:
    print(cliente)


# -------------------------
# ATUALIZAR
# -------------------------

cursor.execute("""
    UPDATE Clientes
    SET email = ?
    WHERE nome = ?
""", ("gabriel.novo@email.com", "Gabriel"))

conexao.commit()

print("\nCliente atualizado com sucesso!")


# -------------------------
# DELETAR
# -------------------------

cursor.execute("""
    DELETE FROM Clientes
    WHERE nome = ?
""", ("Gabriel",))

conexao.commit()

print("Cliente deletado com sucesso!")


# Fechando a conexão
conexao.close()