import sqlite3

# Conectando ao banco
conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

# Criando a tabela caso ainda não exista
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
""")

# Inserindo alguns clientes para realizar os testes
clientes = [
    ("Ana", "ana@email.com"),
    ("Amanda", "amanda@email.com"),
    ("Bruno", "bruno@email.com"),
    ("Carlos", "carlos@email.com"),
    ("Alice", "alice@email.com")
]

cursor.executemany("""
    INSERT INTO Clientes (nome, email)
    VALUES (?, ?)
""", clientes)

conexao.commit()

# Consulta filtrando nomes que começam com A
cursor.execute("""
    SELECT * FROM Clientes
    WHERE nome LIKE 'A%'
""")

clientes_a = cursor.fetchall()

print("Clientes com nome começando com A:")

for cliente in clientes_a:
    print(cliente)

# Fechando a conexão
conexao.close()