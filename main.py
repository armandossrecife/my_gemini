import os
import time
from gemini.manipulador import Gemini

# API endpoint and API key
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
api_key = os.getenv('API_KEY')

# Add the API key to the URL
url_with_key = f"{url}?key={api_key}"

# Instancia a classe que acessa o Gemini
my_gemini = Gemini()

def ask(pergunta: str, url_with_key: str, file_to_save: str):
    t1 = time.time()
    my_gemini.ask_to_gemini(question=pergunta, url_with_key=url_with_key, file_to_save=file_to_save)
    t2 = time.time()
    delta = t2 - t1
    return delta    

try:
    pergunta_usuario = input("Qual a sua pergunta? ")
    
    if pergunta_usuario: 
        pergunta = pergunta_usuario
    else: 
        pergunta = "Explain how AI works"
        
    print(pergunta)
    print(f"Aguarde...")    
    delta = ask(pergunta=pergunta, url_with_key=url_with_key, file_to_save="resposta_prompt")
    print(f"Tempo total de processamento e resposta: {delta:.2f} segundos")
except Exception as ex:
    print(f"Erro ao processar a requisição para o Gemini: {str(ex)}")