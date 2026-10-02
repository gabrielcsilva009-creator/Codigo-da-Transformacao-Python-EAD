try:
    idade = int(input("Digite sua idade: "))

    if idade <= 0:
        raise ValueError("A idade deve ser um número positivo.")

    print(f"Idade válida: {idade} anos.")

except ValueError as erro:
    print(f"Erro: {erro}")