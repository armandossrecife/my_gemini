# Passo 1: Instalar a biblioteca google-generativeai
# Certifique-se de ter a biblioteca google-generativeai instalada.  Se não, execute:
# pip install google-generativeai

# Passo 2: Importar as bibliotecas necessárias
import google.generativeai as genai
import os  # Para manipular variáveis de ambiente (chave da API)

# Passo 3: Configurar a chave da API Gemini
# É fundamental ter uma chave da API Gemini para usar o serviço.
# Você pode obter uma chave em https://makersuite.google.com/app/apikey
# Guarde a chave como uma variável de ambiente para maior segurança.

# Tenta obter a chave da API da variável de ambiente.  Isso é mais seguro do que codificá-la diretamente.
#GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")  # Busca na variável de ambiente
GOOGLE_API_KEY = os.environ.get("API_KEY")  # Busca na variável de ambiente

# Se a variável de ambiente não estiver definida, informe o usuário.
if not GOOGLE_API_KEY:
    print("Erro: A variável de ambiente GOOGLE_API_KEY não está definida.")
    print("Por favor, defina a variável com sua chave da API Gemini.")
    print("Você pode obter uma chave em https://makersuite.google.com/app/apikey")
    exit()  # Encerra o programa se a chave da API não estiver disponível

# Configura a chave da API para o Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Passo 4: Escolher o modelo Gemini
# Define o modelo que será usado.  'gemini-pro' é o modelo padrão para texto.
model = genai.GenerativeModel('gemini-2.0-flash')

# Passo 5: Criar uma função para fazer perguntas e obter respostas
def perguntar_ao_gemini(pergunta):
    """
    Envia uma pergunta para o modelo Gemini e retorna a resposta.

    Args:
        pergunta: A pergunta a ser feita (string).

    Returns:
        A resposta do modelo Gemini (string).  Retorna None em caso de erro.
    """
    try:
        # Gera uma resposta com base na pergunta
        response = model.generate_content(pergunta)

        # Retorna o texto da resposta
        return response.text
    except Exception as e:
        print(f"Erro ao obter resposta do Gemini: {e}")  # Imprime o erro para depuração
        return None


# Passo 6: Interagir com o usuário
if __name__ == "__main__":
    while True:
        # Solicita uma pergunta ao usuário
        pergunta_usuario = input("Faça sua pergunta (ou digite 'sair' para encerrar): ")

        # Verifica se o usuário quer sair
        if pergunta_usuario.lower() == "sair":
            print("Encerrando o programa.")
            break

        # Faz a pergunta ao Gemini e recebe a resposta
        resposta_gemini = perguntar_ao_gemini(pergunta_usuario)

        # Exibe a resposta
        if resposta_gemini:
            print("Resposta do Gemini:")
            print(resposta_gemini)
        else:
            print("Não foi possível obter uma resposta do Gemini.") # Já tratamos o erro na função

        print("-" * 30)  # Separador para melhor leitura