import unittest


class Calculadora:

    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):
        return a / b


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calculadora = Calculadora()

    def test_somar(self):
        resultado = self.calculadora.somar(10, 5)
        self.assertEqual(resultado, 15)

    def test_dividir(self):
        resultado = self.calculadora.dividir(10, 2)
        self.assertEqual(resultado, 5)


if __name__ == "__main__":
    unittest.main()