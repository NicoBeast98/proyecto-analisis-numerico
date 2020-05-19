import unittest
import funciones as f
from calculador import Aproximador
# from parameterized import parameterized


class TestUso(unittest.TestCase):
    def setUp(self):
        self.aprox = Aproximador(
                [1.0, 1.2, 1.4, 1.6, 1.8],
                [0.242, 0.1942, 0.1497, 0.1109, 0.079],
                [f.ln, f.exp(True)], f.unidad)

    def test_error(self):
        self.assertAlmostEqual(
            self.aprox.error(), 0.00494, 5
        )


if __name__ == "__main__":
    unittest.main()
