import unittest
from scraper import extrair_marca, extrair_capacidade
import re

class TestScraperFunctions(unittest.TestCase):

    def test_extrair_marca(self):
        self.assertEqual(extrair_marca("Placa de Vídeo NVIDIA RTX 3060"), "NVIDIA")
        self.assertEqual(extrair_marca("AMD Radeon RX 6700 XT"), "AMD")
        self.assertEqual(extrair_marca("Placa Intel Arc A750"), "Intel")
        self.assertEqual(extrair_marca("Placa Genérica XYZ"), "Desconhecida")

    def test_extrair_capacidade(self):
        self.assertEqual(extrair_capacidade("Placa de Vídeo 8GB NVIDIA"), "8GB")
        self.assertEqual(extrair_capacidade("Radeon RX 6800 XT 16gb"), "16GB")
        self.assertEqual(extrair_capacidade("Geforce RTX 4090 - 24 Gb"), "24GB")
        self.assertEqual(extrair_capacidade("Placa de Vídeo sem info de GB"), "Não informado")

if __name__ == "__main__":
    unittest.main()
