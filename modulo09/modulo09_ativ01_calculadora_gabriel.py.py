def calcular():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    operacao = input("Digite a operação (+, -, *, /): ")

    try:
        if operacao == "+":
            resultado = numero1 + numero2

        elif operacao == "-":
            resultado = numero1 - numero2

        elif operacao == "*":
            resultado = numero1 * numero2

        elif operacao == "/":
            resultado = numero1 / numero2

        else:
            print("Operação inválida!")
            return

        print(f"Resultado: {resultado}")

    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero!")


calcular()