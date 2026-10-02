import sqlite3

# Conectando ao banco de dados
conexao = sqlite3.connect("tarefas.db")
cursor = conexao.cursor()

# Criando a tabela de tarefas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL
    )
""")

conexao.commit()


# -------------------------
# ADICIONAR TAREFA
# -------------------------

def adicionar_tarefa(descricao):
    cursor.execute("""
        INSERT INTO Tarefas (descricao)
        VALUES (?)
    """, (descricao,))

    conexao.commit()

    print("Tarefa adicionada com sucesso!")


# -------------------------
# VISUALIZAR TAREFAS
# -------------------------

def visualizar_tarefas():
    cursor.execute("SELECT * FROM Tarefas")

    tarefas = cursor.fetchall()

    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\nTarefas:")

        for tarefa in tarefas:
            print(f"ID: {tarefa[0]} - {tarefa[1]}")


# -------------------------
# EXCLUIR TAREFA
# -------------------------

def excluir_tarefa(id_tarefa):
    cursor.execute("""
        DELETE FROM Tarefas
        WHERE id = ?
    """, (id_tarefa,))

    conexao.commit()

    if cursor.rowcount > 0:
        print("Tarefa excluída com sucesso!")
    else:
        print("Tarefa não encontrada.")


# -------------------------
# MENU
# -------------------------

while True:
    print("\n===== GERENCIADOR DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Visualizar tarefas")
    print("3 - Excluir tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        descricao = input("Digite a tarefa: ")
        adicionar_tarefa(descricao)

    elif opcao == "2":
        visualizar_tarefas()

    elif opcao == "3":
        id_tarefa = int(input("Digite o ID da tarefa que deseja excluir: "))
        excluir_tarefa(id_tarefa)

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")


# Fechando o banco
conexao.close()