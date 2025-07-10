import unittest
from area import calcular_area_cuadrado, calcular_area_circulo, calcular_area_triangulo

class TestAreas(unittest.TestCase):
    # Pruebas para área del cuadrado
    def test_calcular_area_cuadrado_valido(self):
        self.assertEqual(calcular_area_cuadrado(5), 25)

    def test_calcular_area_cuadrado_invalido(self):
        self.assertIsNone(calcular_area_cuadrado(-3))

    # Pruebas para área del círculo
    def test_calcular_area_circulo_valido(self):
        self.assertAlmostEqual(calcular_area_circulo(1), 3.14159, places=4)

    def test_calcular_area_circulo_invalido(self):
        self.assertIsNone(calcular_area_circulo(0))

    # Pruebas para área del triángulo
    def test_calcular_area_triangulo_valido(self):
        self.assertEqual(calcular_area_triangulo(4, 3), 6)

    def test_calcular_area_triangulo_invalido(self):
        self.assertIsNone(calcular_area_triangulo(-1, 2))

if __name__ == '__main__':
    unittest.main()
