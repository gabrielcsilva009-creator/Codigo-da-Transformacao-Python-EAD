def maior_menor(numeros):
    maior = max(numeros)
    menor = min(numeros)

    return maior, menor


numeros = [10, 5, 20, 8, 15]

maior, menor = maior_menor(numeros)

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")