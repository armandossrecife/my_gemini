from utilidades.texto import Utils
from utilidades.tempo import Tempo
import requests
import json

class Gemini():
    def __init__(self):
        self.utilidades_texto = Utils()
        self.tempo = Tempo()
        self.instante = None
        # Headers for the request
        self.headers = {
            "Content-Type": "application/json"
        }
        
    def set_instante(self, valor):
        self.instante = valor

    def set_payload(self, prompt: str):
        # Payload (data) for the request
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }
        return payload

    def ask_to_gemini(self, question: str, url_with_key: str, file_to_save: str):
        # set the payload
        payload = self.set_payload(prompt=question)

        print("Acessando o Gemini...")
        # Send the POST request
        response = requests.post(url_with_key, headers=self.headers, json=payload)

        # Check if the request was successful
        if response.status_code == 200:
            # Print the response from the API
            print("Response from Gemini API:")
            self.set_instante(self.tempo.get_current_date_and_time())
            self.utilidades_texto.save_text_in_file_based_time(content=response.json(), tempo=self.instante)
            response_json = response.json()
                    
            # Check if response_json is a string and parse it
            if isinstance(response_json, str):
                response_data = json.loads(response_json)
            else:
                response_data = response_json

            # Extract the generated text from the "parts" array
            generated_text = response_data["candidates"][0]["content"]["parts"][0]["text"]

            # Print the extracted text
            print("Generated Text:")
            print(generated_text)
            
            self.utilidades_texto.convert_text_to_markdown(generated_text=generated_text, filename=file_to_save, tempo=self.instante)            
        else:
            # Print the error message
            print(f"Error: {response.status_code}")
            print(response.text)   