import unittest


class Calculadora:

    def dividir(self, a, b):
        return a / b


class TestDivisao(unittest.TestCase):

    def test_divisao_por_zero(self):
        calculadora = Calculadora()

        with self.assertRaises(ZeroDivisionError):
            calculadora.dividir(10, 0)


if __name__ == "__main__":
    unittest.main()