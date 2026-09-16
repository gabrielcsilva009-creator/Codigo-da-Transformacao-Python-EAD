class Carro:
    def __init__(self,marca, modelo):
        self.marca = marca
        self.modelo =  modelo


    def exibir_(self):
        return f"Marca: {self.marca}, Modelo:"
        {self.modelo}

        #meu_carro = Carro ("chevrolet", "carro")
        meu_carro = Carro("Ford", "Mustang")
        print(meu_carro.exibir_info())