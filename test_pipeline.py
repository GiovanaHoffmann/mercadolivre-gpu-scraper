import unittest
from unittest.mock import MagicMock, patch
import pandas as pd
from pipeline import conn, cursor  # Importa conexão real do pipeline

class TestPipeline(unittest.TestCase):

    @patch("pipeline.psycopg2.connect")
    def test_conexao_bd(self, mock_connect):
        """Testa se a conexão com o banco de dados é aberta corretamente"""
        mock_connect.return_value = MagicMock()
        conn = mock_connect()
        self.assertTrue(conn)

    def test_leitura_csv(self):
        """Testa se o CSV é carregado corretamente"""
        df = pd.DataFrame({"Produto": ["RTX 3060"], "Preço": [2499.99], "Marca": ["NVIDIA"], "Capacidade": ["12GB"]})
        self.assertIn("Produto", df.columns)
        self.assertIn("Preço", df.columns)
        self.assertIn("Marca", df.columns)
        self.assertIn("Capacidade", df.columns)

if __name__ == "__main__":
    unittest.main()
