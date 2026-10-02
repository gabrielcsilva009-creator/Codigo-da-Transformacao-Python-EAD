usuarios = {
    "gabriel": "1234",
    "joao": "5678",
    "maria": "abcd"
}


def validar_login(usuario, senha):
    if usuario not in usuarios or usuarios[usuario] != senha:
        raise ValueError("Usuário ou senha incorretos!")

    return True


tentativas = 3

while tentativas > 0:
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

    try:
        validar_login(usuario, senha)

        print("Login realizado com sucesso!")
        break

    except ValueError as erro:
        tentativas -= 1

        print(f"Erro: {erro}")
        print(f"Tentativas restantes: {tentativas}")

else:
    print("Número máximo de tentativas atingido. Acesso bloqueado.")