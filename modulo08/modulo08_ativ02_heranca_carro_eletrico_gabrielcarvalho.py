class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"


class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Autonomia: {self.autonomia_bateria} km"


meu_carro_eletrico = CarroEletrico("Tesla", "Model 3", 500)

print(meu_carro_eletrico.exibir_info())