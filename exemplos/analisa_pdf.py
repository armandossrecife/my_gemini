import google.generativeai as genai
import httpx
import os

# Certifique-se de que a variável de ambiente API_KEY está configurada corretamente
API_KEY = os.getenv('API_KEY')
if not API_KEY:
    raise ValueError("API_KEY não encontrada. Certifique-se de configurar a variável de ambiente.")

# Inicialize o cliente da API
genai.configure(api_key=API_KEY)

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"  # Substitua pela URL real do seu PDF

prompt = "Resuma este documento"

try:
    print("Lendo o pdf...")
    # Baixe o PDF diretamente para a memória
    response = httpx.get(doc_url)
    response.raise_for_status()  # Lança uma exceção para erros HTTP 4xx e 5xx

    if response.headers.get("Content-Type") != "application/pdf":
        raise ValueError("A URL fornecida não retorna um arquivo PDF.")

    pdf_bytes = response.content

    # Crie um modelo
    model = genai.GenerativeModel('gemini-2.0-flash') #Use gemini-pro-vision if available for pdf processing.

    print("Aguarde o processamento...")
    # Prepare a entrada para o modelo
    response = model.generate_content(
        contents=[
          {
              "mime_type": "application/pdf",
              "data": pdf_bytes
          },
          prompt
        ]
    )

    print(response.text)

except httpx.RequestError as e:
    print(f"Erro ao baixar o PDF: {e}")
except FileNotFoundError:
    print("Arquivo PDF não encontrado.")
except ValueError as e:
    print(f"Erro de valor: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")