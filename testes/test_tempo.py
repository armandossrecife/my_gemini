import unittest
from datetime import datetime
from utilidades.tempo import Tempo  # Importa a classe Tempo do módulo tempo.py

class TestTempo(unittest.TestCase):
    def setUp(self):
        """
        Configura o ambiente de teste. 
        Este método é executado antes de cada teste.
        """
        self.tempo = Tempo()  # Cria uma instância da classe Tempo

    def test_get_current_date_and_time_format(self):
        """
        Testa se o método get_current_date_and_time retorna uma string no formato YYYY-MM-DD_HH-MM-SS.
        """
        # Obtém a data e hora formatadas
        resultado = self.tempo.get_current_date_and_time()

        # Verifica se o resultado é uma string
        self.assertIsInstance(resultado, str, "O resultado deve ser uma string.")

        # Verifica o formato da string usando uma expressão regular
        import re
        formato_esperado = r"\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}"
        self.assertTrue(re.match(formato_esperado, resultado), f"O formato da string '{resultado}' não corresponde ao esperado (YYYY-MM-DD_HH-MM-SS).")

    def test_get_current_date_and_time_value(self):
        """
        Testa se o valor retornado pelo método get_current_date_and_time é consistente com a data e hora atuais.
        """
        # Obtém a data e hora atuais
        agora = datetime.now()
        valor_esperado = agora.strftime("%Y-%m-%d_%H-%M-%S")

        # Obtém o valor retornado pelo método
        resultado = self.tempo.get_current_date_and_time()

        # Verifica se o valor retornado é consistente com o valor esperado
        self.assertEqual(resultado, valor_esperado, f"O valor retornado '{resultado}' não corresponde ao valor esperado '{valor_esperado}'.")

if __name__ == "__main__":
    unittest.main()