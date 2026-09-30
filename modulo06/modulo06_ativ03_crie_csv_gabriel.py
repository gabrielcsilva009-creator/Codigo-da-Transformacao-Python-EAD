import csv


# Lista para armazenar as notas
notas = []


# Quantidade de alunos
quantidade = int(input("Quantos alunos deseja cadastrar? "))


# Cadastrando os alunos
for i in range(quantidade):
    print(f"\nAluno {i + 1}")

    nome = input("Nome do aluno: ")
    nota = float(input("Nota do aluno: "))

    notas.append([nome, nota])


# Salvando os dados no arquivo CSV
with open("notas.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)

    escritor.writerow(["Nome", "Nota"])

    for aluno in notas:
        escritor.writerow(aluno)


print("\nNotas salvas com sucesso!")


# Carregando e exibindo os dados
print("\n--- NOTAS DOS ALUNOS ---")

with open("notas.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)

    next(leitor)  # Pula o cabeçalho

    for linha in leitor:
        nome = linha[0]
        nota = linha[1]

        print(f"Aluno: {nome} | Nota: {nota}")