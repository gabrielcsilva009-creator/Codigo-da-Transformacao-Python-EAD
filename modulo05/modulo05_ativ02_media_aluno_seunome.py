def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3

    print(f"Média: {media:.2f}")

    if media >= 7:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")


calcular_media(8, 7, 9)