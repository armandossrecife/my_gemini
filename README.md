# my_gemini
Acessa a LLM do Gemini

## 1. Crie uma chave de acesso ao Gemini

No Google AI Studio (https://aistudio.google.com/apikey) crie uma chave

## 2. Crie uma variável de ambiente API_KEY

```bash
export API_KEY=sua_chave...
```

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## 4. Execute o script principal

```bash
python3 main.py
```
```bash
Qual a sua pergunta?
```

## Resultados

Caso a execução seja feita com sucesso, o programa vai gerar as respostas em dois arquivos: 
- .json contendo o resultado do Gemini
- .md contendo a resposta em Markdown
