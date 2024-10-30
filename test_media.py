import unittest
from media import calcular_media

class TestMedia(unittest.TestCase):

    print("Digite as três notas para calcular a média:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    
    media = calcular_media(nota1, nota2, nota3)
    print(f"A média das três notas é: {media:.2f}")

    def test_media_basica(self):
        self.assertEqual(calcular_media(7, 8, 9), 8.0)  # Teste com valores comuns

    def test_media_todas_zero(self):
        self.assertEqual(calcular_media(0, 0, 0), 0.0)  # Teste com todas as notas sendo zero

    def test_media_maxima(self):
        self.assertEqual(calcular_media(10, 10, 10), 10.0)  # Teste com todas as notas no valor máximo

    def test_media_valores_decimais(self):
        self.assertAlmostEqual(calcular_media(7.5, 8.5, 9.0), 8.33, places=2)  # Teste com valores decimais e arredondamento

if __name__ == '__main__':
    unittest.main()