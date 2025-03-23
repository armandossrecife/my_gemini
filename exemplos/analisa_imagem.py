from PIL import Image
import google.generativeai as genai
import os

# Certifique-se de que a variável de ambiente API_KEY está configurada corretamente
API_KEY = os.getenv('API_KEY')
if not API_KEY:
    raise ValueError("API_KEY não encontrada. Certifique-se de configurar a variável de ambiente.")

# Inicialize o cliente da API
genai.configure(api_key=API_KEY)

# Carregue a imagem
try:
    image = Image.open("imagens/carro.jpg")  # Certifique-se de que o caminho da imagem está correto
except FileNotFoundError:
    raise FileNotFoundError("Arquivo de imagem não encontrado. Verifique o caminho.")

# Gere o conteúdo usando o modelo Gemini
try:
    # Crie um modelo
    model = genai.GenerativeModel('gemini-2.0-flash')

    # Prepare a entrada para o modelo
    response = model.generate_content(["Tell me about this picture", image])

    # Exiba a resposta
    print(response.text)
except Exception as e:
    print(f"Erro ao gerar conteúdo: {e}")