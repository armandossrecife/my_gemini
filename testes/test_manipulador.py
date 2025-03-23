import unittest
from unittest.mock import patch, Mock
from gemini.manipulador import Gemini  # Importa a classe Gemini do módulo manipulador.py
import os

class TestGemini(unittest.TestCase):
    def setUp(self):
        """
        Configura o ambiente de teste. 
        Este método é executado antes de cada teste.
        """
        api_key = os.getenv('API_KEY')
        self.gemini = Gemini()  # Cria uma instância da classe Gemini
        self.question = "Qual é a capital da França?"
        self.url_with_key = f"https://api.gemini.com/v1/ask?key={api_key}"
        self.file_to_save = "resposta_gemini"

    @patch("requests.post")  # Simula a requisição HTTP
    def test_ask_to_gemini_success(self, mock_post):
        """
        Testa o método ask_to_gemini em caso de sucesso na requisição.
        """
        # Configura o mock para simular uma resposta bem-sucedida
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {"text": "A capital da França é Paris."}
                        ]
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        # Executa o método a ser testado
        self.gemini.ask_to_gemini(self.question, self.url_with_key, self.file_to_save)

        # Verifica se a requisição foi feita corretamente
        mock_post.assert_called_once_with(
            self.url_with_key,
            headers={"Content-Type": "application/json"},
            json={
                "contents": [
                    {
                        "parts": [
                            {"text": self.question}
                        ]
                    }
                ]
            }
        )

        # Verifica se o instante foi definido
        self.assertIsNotNone(self.gemini.instante)

    @patch("requests.post")  # Simula a requisição HTTP
    def test_ask_to_gemini_failure(self, mock_post):
        """
        Testa o método ask_to_gemini em caso de falha na requisição.
        """
        # Configura o mock para simular uma resposta com erro
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_post.return_value = mock_response

        # Executa o método a ser testado
        self.gemini.ask_to_gemini(self.question, self.url_with_key, self.file_to_save)

        # Verifica se a requisição foi feita corretamente
        mock_post.assert_called_once_with(
            self.url_with_key,
            headers={"Content-Type": "application/json"},
            json={
                "contents": [
                    {
                        "parts": [
                            {"text": self.question}
                        ]
                    }
                ]
            }
        )

        # Verifica se o erro foi tratado corretamente
        self.assertIsNone(self.gemini.instante)

if __name__ == "__main__":
    unittest.main()