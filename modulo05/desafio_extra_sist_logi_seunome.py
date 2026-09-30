# Dicionário com os usuários e suas respectivas senhas
usuarios = {
    "gabriel": "1234",
    "joao": "5678",
    "maria": "abcd"
}


# Função para validar o login
def validar_login(usuario, senha):
    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login realizado com sucesso!")
    else:
        print("Usuário ou senha incorretos!")


# Pedindo os dados ao usuário
usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

# Verificando o login
validar_login(usuario, senha)