import unittest
import json
import os
from utilidades.texto import Utils  # Importa a classe Utils do módulo texto.py

class TestUtils(unittest.TestCase):
    def setUp(self):
        """
        Configura o ambiente de teste. 
        Este método é executado antes de cada teste.
        """
        self.utils = Utils()  # Cria uma instância da classe Utils
        self.tempo = "2023-10-25_14-30-45"  # Timestamp fixo para testes
        self.filename = "test_file"  # Nome base do arquivo para testes

    def tearDown(self):
        """
        Limpa o ambiente de teste.
        Este método é executado após cada teste.
        """
        # Remove os arquivos criados durante os testes, se existirem
        if os.path.exists(f"{self.tempo}.json"):
            os.remove(f"{self.tempo}.json")
        if os.path.exists(f"{self.filename}_{self.tempo}.md"):
            os.remove(f"{self.filename}_{self.tempo}.md")

    def test_save_text_in_file_based_time_with_dict(self):
        """
        Testa o método save_text_in_file_based_time com um dicionário como conteúdo.
        """
        content = {"resposta": "A capital da França é Paris."}
        self.utils.save_text_in_file_based_time(content, self.tempo)

        # Verifica se o arquivo foi criado
        self.assertTrue(os.path.exists(f"{self.tempo}.json"), "O arquivo JSON não foi criado.")

        # Verifica o conteúdo do arquivo
        with open(f"{self.tempo}.json", "r", encoding="utf-8") as file:
            file_content = file.read()
            self.assertEqual(json.loads(file_content), content, "O conteúdo do arquivo JSON não corresponde ao esperado.")

    def test_save_text_in_file_based_time_with_string(self):
        """
        Testa o método save_text_in_file_based_time com uma string como conteúdo.
        """
        content = '{"resposta": "A capital da França é Paris."}'
        self.utils.save_text_in_file_based_time(content, self.tempo)

        # Verifica se o arquivo foi criado
        self.assertTrue(os.path.exists(f"{self.tempo}.json"), "O arquivo JSON não foi criado.")

        # Verifica o conteúdo do arquivo
        with open(f"{self.tempo}.json", "r", encoding="utf-8") as file:
            file_content = file.read()
            self.assertEqual(file_content, content, "O conteúdo do arquivo JSON não corresponde ao esperado.")

    def test_convert_text_to_markdown(self):
        """
        Testa o método convert_text_to_markdown.
        """
        generated_text = "# Resposta do Gemini\n\nA capital da França é Paris."
        self.utils.convert_text_to_markdown(generated_text, self.filename, self.tempo)

        # Verifica se o arquivo Markdown foi criado
        self.assertTrue(os.path.exists(f"{self.filename}_{self.tempo}.md"), "O arquivo Markdown não foi criado.")

        # Verifica o conteúdo do arquivo
        with open(f"{self.filename}_{self.tempo}.md", "r", encoding="utf-8") as file:
            file_content = file.read()
            self.assertEqual(file_content, generated_text, "O conteúdo do arquivo Markdown não corresponde ao esperado.")

    def test_save_text_in_file_based_time_error(self):
        """
        Testa o método save_text_in_file_based_time em caso de erro.
        """
        # Tenta salvar em um caminho inválido para forçar um erro
        with self.assertRaises(ValueError, msg="O método não levantou uma exceção ao encontrar um erro."):
            self.utils.save_text_in_file_based_time({"resposta": "Teste"}, "/caminho/invalido/arquivo.json")

    def test_convert_text_to_markdown_error(self):
        """
        Testa o método convert_text_to_markdown em caso de erro.
        """
        # Tenta salvar em um caminho inválido para forçar um erro
        with self.assertRaises(ValueError, msg="O método não levantou uma exceção ao encontrar um erro."):
            self.utils.convert_text_to_markdown("Teste", "/caminho/invalido/arquivo", self.tempo)

if __name__ == "__main__":
    unittest.main()