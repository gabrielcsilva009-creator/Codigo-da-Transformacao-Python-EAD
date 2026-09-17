idade = int(input("Digite a sua idade: "))

if idade < 13:
    print("você é uma criança.")
elif idade < 18:
    print("você é um adolescente.")
elif idade < 60:
    print("você é um adulto")
else:
    print("você é um idoso")