## Documentação do Projeto

### Visão Geral
Este projeto é uma aplicação Python que faz perguntas para o Gemini (um modelo de linguagem), exibe as respostas para o usuário e salva os retornos em dois formatos: `.json` (para estrutura de dados) e `.md` (para leitura humana). A aplicação é organizada em módulos para facilitar a manutenção e a escalabilidade.

---

## Estrutura do Projeto

```
├── README.md                   # Documentação do projeto
├── main.py                     # Ponto de entrada da aplicação
├── requirements.txt            # Dependências do projeto
├── gemini                      # Módulo para interação com o Gemini
│   ├── __init__.py             # Inicialização do módulo
│   └── manipulador.py          # Lógica para fazer perguntas e processar respostas
├── utilidades
│   ├── __init__.py             # Inicialização do módulo
│   ├── tempo.py                # Funções relacionadas a data e hora
│   ├── texto.py                # Funções para manipulação de texto
├── testes                      # Testes automáticos da aplicação
│   ├── test_manipulador.py     # Testes automáticos do módulo gemini/manipulador.py
│   ├── test_texto.py           # Testes automáticos do módulo utilidades/texto.py
│   ├── test_tempo.py           # Testes automáticos do módulo utilidades/tempo.py
└── respostas                   # Pasta para armazenar respostas do Gemini
    ├── 2025-03-23_11-14-10.json
    ├── 2025-03-23_11-32-07.json
    ├── resposta_prompt_2025-03-23_11-14-10.md
    └── resposta_prompt_2025-03-23_11-32-07.md
```
---

## Como Usar

### Pré-requisitos
1. Python 3.x instalado.
2. Dependências instaladas (execute `pip install -r requirements.txt`).

### Executando o Projeto
1. Clone o repositório ou baixe os arquivos do projeto.
2. No terminal, navegue até a pasta raiz do projeto.
3. Execute o arquivo `main.py`:
   ```bash
   python main.py
   ```
4. Siga as instruções exibidas no terminal para fazer uma pergunta ao Gemini.

---

## Módulos Principais

### `main.py`
- **Função**: Ponto de entrada da aplicação.
- **Responsabilidade**: Coordena a interação com o usuário, chama o manipulador do Gemini e salva as respostas.

### `gemini/manipulador.py`
- **Função**: Gerencia a comunicação com o Gemini.

### `utilidades/tempo.py`
- **Função**: Fornece funções relacionadas a data e hora.

### `utilidades/texto.py`
- **Função**: Fornece funções para manipulação de texto.

---

## Exemplo de Uso

1. Execute o projeto:
   ```bash
   python main.py
   ```
2. Insira uma pergunta quando solicitado:
   ```
   Digite sua pergunta: Qual é a capital da França?
   ```
3. A resposta será exibida no terminal e salva na pasta `respostas`:
   - `2025-03-23_11-14-10.json`: Resposta no formato JSON.
   - `resposta_prompt_2025-03-23_11-14-10.md`: Resposta formatada em Markdown.

---

## Execução dos testes automáticos

No diretório principal do projeto: 

```bash
python3 run_tests.py
```

## Dependências
As dependências do projeto estão listadas no arquivo `requirements.txt`. Para instalá-las, execute:
```bash
pip install -r requirements.txt
```

---

## Contribuição
1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

---

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

---

## Módulo `gemini/manipulador.py`

### Descrição
Este módulo contém a classe `Gemini`, responsável por interagir com a API do Gemini. Ele envia perguntas, processa as respostas e salva os resultados em arquivos `.json` e `.md`.

---

### Classe `Gemini`

#### Atributos
- **`utilidades_texto`**: Instância da classe `Utils` do módulo `utilidades.texto`, usada para manipulação de texto.
- **`tempo`**: Instância da classe `Tempo` do módulo `utilidades.tempo`, usada para gerar timestamps.
- **`instante`**: Armazena o timestamp atual gerado durante a execução.
- **`headers`**: Cabeçalhos HTTP usados na requisição para a API do Gemini.

---

#### Métodos

##### `__init__()`
Inicializa a classe `Gemini`.
- **Atribui**:
  - `utilidades_texto`: Instância de `Utils`.
  - `tempo`: Instância de `Tempo`.
  - `instante`: Inicializado como `None`.
  - `headers`: Define o cabeçalho `Content-Type` como `application/json`.

---

##### `set_instante(valor)`
Define o valor do atributo `instante`.
- **Parâmetros**:
  - `valor` (str): Timestamp a ser armazenado.
- **Uso**:
  ```python
  gemini = Gemini()
  gemini.set_instante("2025-03-23_11-14-10")
  ```

---

##### `set_payload(prompt: str)`
Cria o payload (corpo da requisição) para enviar ao Gemini.
- **Parâmetros**:
  - `prompt` (str): A pergunta a ser enviada ao Gemini.
- **Retorna**:
  - `dict`: Payload no formato esperado pela API do Gemini.
- **Exemplo**:
  ```python
  payload = gemini.set_payload("Qual é a capital da França?")
  ```

---

##### `ask_to_gemini(question: str, url_with_key: str, file_to_save: str)`
Envia uma pergunta ao Gemini, processa a resposta e salva os resultados.
- **Parâmetros**:
  - `question` (str): A pergunta a ser enviada.
  - `url_with_key` (str): URL da API do Gemini, incluindo a chave de autenticação.
  - `file_to_save` (str): Nome base do arquivo para salvar a resposta.
- **Funcionamento**:
  1. Define o payload usando `set_payload`.
  2. Envia uma requisição POST para a API do Gemini.
  3. Se a requisição for bem-sucedida (status code 200):
     - Gera um timestamp usando `Tempo`.
     - Salva a resposta JSON em um arquivo.
     - Extrai o texto gerado da resposta.
     - Converte o texto para Markdown e salva em um arquivo.
  4. Se a requisição falhar, exibe uma mensagem de erro.
- **Exemplo**:
  ```python
  gemini = Gemini()
  gemini.ask_to_gemini(
      question="Qual é a capital da França?",
      url_with_key="https://api.gemini.com/v1/ask?key=SUA_CHAVE_AQUI",
      file_to_save="resposta_gemini"
  )
  ```

---

### Exemplo de Uso Completo

```python
from gemini.manipulador import Gemini

# Cria uma instância da classe Gemini
gemini = Gemini()

# Define a pergunta e a URL da API (com chave de autenticação)
pergunta = "Qual é a capital da França?"
url_api = "https://api.gemini.com/v1/ask?key=SUA_CHAVE_AQUI"

# Envia a pergunta ao Gemini e salva a resposta
gemini.ask_to_gemini(
    question=pergunta,
    url_with_key=url_api,
    file_to_save="resposta_gemini"
)
```

---

### Fluxo de Funcionamento
1. O método `ask_to_gemini` é chamado com a pergunta, URL da API e nome do arquivo.
2. O payload é criado com a pergunta.
3. A requisição POST é enviada para a API do Gemini.
4. Se a resposta for bem-sucedida:
   - O timestamp é gerado.
   - A resposta JSON é salva em um arquivo.
   - O texto gerado é extraído e salvo em um arquivo Markdown.
5. Se a resposta falhar, uma mensagem de erro é exibida.

---

### Exemplo de Saída
- **Arquivo JSON** (`respostas/2025-03-23_11-14-10.json`):
  ```json
  {
    "candidates": [
      {
        "content": {
          "parts": [
            {
              "text": "A capital da França é Paris."
            }
          ]
        }
      }
    ]
  }
  ```

- **Arquivo Markdown** (`respostas/resposta_prompt_2025-03-23_11-14-10.md`):
  ```markdown
  # Resposta do Gemini

  A capital da França é Paris.
  ```

---

### Tratamento de Erros
- Se a requisição falhar (status code diferente de 200), o método exibe:
  - O código de status.
  - A mensagem de erro retornada pela API.

---

### Dependências
- **`requests`**: Para enviar requisições HTTP.
- **`json`**: Para manipulação de dados JSON.
- **`utilidades.texto.Utils`**: Para manipulação de texto e salvamento de arquivos.
- **`utilidades.tempo.Tempo`**: Para geração de timestamps.

---

### Melhorias Futuras
- Adicionar suporte para múltiplas perguntas em uma única requisição.
- Implementar tratamento de erros mais robusto.
- Adicionar suporte para diferentes formatos de saída (e.g., HTML, PDF).

---

## Módulo `utilidades/tempo.py`

### Descrição
Este módulo contém a classe `Tempo`, que fornece funcionalidades relacionadas à manipulação de data e hora. Atualmente, ele inclui um método para obter a data e hora atuais em um formato específico.

---

### Classe `Tempo`

#### Métodos

##### `get_current_date_and_time()`
Retorna a data e hora atuais no formato `YYYY-MM-DD_HH-MM-SS`.
- **Retorna**:
  - `str`: Data e hora formatadas como uma string (e.g., `"2023-10-25_14-30-45"`).
- **Funcionamento**:
  1. Obtém a data e hora atuais usando `datetime.now()`.
  2. Formata a data e hora no padrão `YYYY-MM-DD_HH-MM-SS`.
- **Exemplo**:
  ```python
  tempo = Tempo()
  timestamp = tempo.get_current_date_and_time()
  print(timestamp)  # Saída: "2023-10-25_14-30-45"
  ```

---

### Exemplo de Uso Completo

```python
from utilidades.tempo import Tempo

# Cria uma instância da classe Tempo
tempo = Tempo()

# Obtém a data e hora atuais formatadas
timestamp = tempo.get_current_date_and_time()

# Exibe o resultado
print("Timestamp atual:", timestamp)
```

---

### Fluxo de Funcionamento
1. O método `get_current_date_and_time` é chamado.
2. A data e hora atuais são obtidas usando `datetime.now()`.
3. A data e hora são formatadas no padrão `YYYY-MM-DD_HH-MM-SS`.
4. O valor formatado é retornado como uma string.

---

### Exemplo de Saída
- **Saída no console**:
  ```
  Timestamp atual: 2023-10-25_14-30-45
  ```

---

### Dependências
- **`datetime`**: Módulo da biblioteca padrão do Python para manipulação de datas e horas.

---

### Melhorias Futuras
- Adicionar métodos para formatar datas e horas em outros padrões (e.g., `DD/MM/YYYY`, `HH:MM:SS`).
- Implementar funcionalidades para cálculos de diferença entre datas.
- Adicionar suporte para fusos horários.

---

### Documentação no Código
Aqui está o código do módulo `tempo.py` com comentários adicionais para melhorar a clareza:

```python
from datetime import datetime

class Tempo():
    def __init__(self):
        """
        Inicializa a classe Tempo.
        """
        pass
    
    def get_current_date_and_time(self):
        """
        Retorna a data e hora atuais no formato YYYY-MM-DD_HH-MM-SS.

        Returns:
            str: Data e hora formatadas como uma string.
        """
        # Obtém a data e hora atuais
        now = datetime.now()
        # Formata a data e hora no padrão YYYY-MM-DD_HH-MM-SS
        valor = now.strftime("%Y-%m-%d_%H-%M-%S")
        return valor
```

---

## Módulo `utilidades/texto.py`

### Descrição
Este módulo contém a classe `Utils`, que fornece funcionalidades para manipulação de texto, incluindo a gravação de conteúdo em arquivos JSON e a conversão de texto para o formato Markdown.

---

### Classe `Utils`

#### Métodos

##### `save_text_in_file_based_time(content, tempo)`
Salva o conteúdo fornecido em um arquivo JSON, utilizando um timestamp como parte do nome do arquivo.
- **Parâmetros**:
  - `content` (dict ou str): Conteúdo a ser salvo. Se for um dicionário, será convertido para uma string JSON formatada.
  - `tempo` (str): Timestamp a ser usado no nome do arquivo.
- **Funcionamento**:
  1. Verifica se o conteúdo é um dicionário e, se for, converte-o para uma string JSON formatada.
  2. Salva o conteúdo em um arquivo com o nome no formato `tempo.json`.
  3. Em caso de erro, lança uma exceção com uma mensagem descritiva.
- **Exemplo**:
  ```python
  utils = Utils()
  conteudo = {"resposta": "A capital da França é Paris."}
  utils.save_text_in_file_based_time(conteudo, "2023-10-25_14-30-45")
  ```

---

##### `convert_text_to_markdown(generated_text: str, filename: str, tempo: str)`
Converte um texto em formato Markdown e salva em um arquivo com um nome baseado no timestamp.
- **Parâmetros**:
  - `generated_text` (str): Texto a ser salvo no arquivo Markdown.
  - `filename` (str): Nome base do arquivo.
  - `tempo` (str): Timestamp a ser usado no nome do arquivo.
- **Funcionamento**:
  1. Cria um arquivo Markdown com o nome no formato `filename_tempo.md`.
  2. Salva o texto no arquivo Markdown.
  3. Em caso de erro, lança uma exceção com uma mensagem descritiva.
- **Exemplo**:
  ```python
  utils = Utils()
  texto = "# Resposta do Gemini\n\nA capital da França é Paris."
  utils.convert_text_to_markdown(texto, "resposta_gemini", "2023-10-25_14-30-45")
  ```

---

### Exemplo de Uso Completo

```python
from utilidades.texto import Utils

# Cria uma instância da classe Utils
utils = Utils()

# Exemplo de uso do save_text_in_file_based_time
conteudo_json = {"resposta": "A capital da França é Paris."}
utils.save_text_in_file_based_time(conteudo_json, "2023-10-25_14-30-45")

# Exemplo de uso do convert_text_to_markdown
texto_markdown = "# Resposta do Gemini\n\nA capital da França é Paris."
utils.convert_text_to_markdown(texto_markdown, "resposta_gemini", "2023-10-25_14-30-45")
```

---

### Fluxo de Funcionamento

#### `save_text_in_file_based_time`
1. Recebe o conteúdo e o timestamp.
2. Converte o conteúdo para JSON, se necessário.
3. Salva o conteúdo em um arquivo com o nome `tempo.json`.
4. Exibe uma mensagem de confirmação ou lança uma exceção em caso de erro.

#### `convert_text_to_markdown`
1. Recebe o texto, o nome base do arquivo e o timestamp.
2. Cria um arquivo Markdown com o nome `filename_tempo.md`.
3. Salva o texto no arquivo Markdown.
4. Exibe uma mensagem de confirmação ou lança uma exceção em caso de erro.

---

### Exemplo de Saída

#### `save_text_in_file_based_time`
- **Arquivo salvo**: `2023-10-25_14-30-45.json`
- **Conteúdo**:
  ```json
  {
      "resposta": "A capital da França é Paris."
  }
  ```

#### `convert_text_to_markdown`
- **Arquivo salvo**: `resposta_gemini_2023-10-25_14-30-45.md`
- **Conteúdo**:
  ```markdown
  # Resposta do Gemini

  A capital da França é Paris.
  ```

---

### Dependências
- **`json`**: Módulo da biblioteca padrão do Python para manipulação de dados JSON.

---

### Melhorias Futuras
- Adicionar suporte para outros formatos de arquivo (e.g., XML, YAML).
- Implementar funcionalidades para leitura de arquivos.
- Adicionar tratamento de erros mais detalhado.

---

### Documentação no Código
Aqui está o código do módulo `texto.py` com comentários adicionais para melhorar a clareza:

```python
import json

class Utils():
    def __init__(self):
        """
        Inicializa a classe Utils.
        """
        pass
    
    def save_text_in_file_based_time(self, content, tempo):
        """
        Salva o conteúdo em um arquivo JSON com base no timestamp fornecido.

        Args:
            content (dict ou str): Conteúdo a ser salvo.
            tempo (str): Timestamp a ser usado no nome do arquivo.

        Raises:
            ValueError: Se ocorrer um erro ao salvar o arquivo.
        """
        file_name = tempo + ".json"
        try:
            # Converte o conteúdo para JSON, se for um dicionário
            if isinstance(content, dict):
                content = json.dumps(content, indent=4)  # Formata o JSON
            # Salva o conteúdo no arquivo
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(content)
            print(f"File saved as {file_name}")
        except Exception as ex:
            raise ValueError(f"Error saving content to file: {str(ex)}")

    def convert_text_to_markdown(self, generated_text: str, filename: str, tempo: str):
        """
        Converte um texto para Markdown e salva em um arquivo com base no timestamp.

        Args:
            generated_text (str): Texto a ser salvo.
            filename (str): Nome base do arquivo.
            tempo (str): Timestamp a ser usado no nome do arquivo.

        Raises:
            ValueError: Se ocorrer um erro ao salvar o arquivo.
        """
        try:
            # Cria o caminho do arquivo Markdown
            markdown_file_path = f"{filename}_{tempo}.md"
            # Salva o texto no arquivo Markdown
            with open(markdown_file_path, "w", encoding="utf-8") as md_file:
                md_file.write(generated_text)
            print(f"Markdown file saved as {markdown_file_path}")        
        except Exception as ex:
            raise ValueError(f"Erro ao converter o texto para markdown: {str(ex)}")
```