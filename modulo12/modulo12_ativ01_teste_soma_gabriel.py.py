import unittest


def somar(a, b):
    return a + b


class TestSoma(unittest.TestCase):

    def test_soma(self):
        resultado = somar(5, 3)
        self.assertEqual(resultado, 8)


if __name__ == "__main__":
    unittest.main()