from seguranca.gerador import gerar_senha
from seguranca.validador import validar_senha


tamanho = int(input("Digite o tamanho da senha: "))

senha = gerar_senha(tamanho)

print(f"Senha gerada: {senha}")

if validar_senha(senha):
    print("A senha é segura!")
else:
    print("A senha não é segura!")