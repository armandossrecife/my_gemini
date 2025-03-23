from google import genai

client = genai.Client()
myfile = client.files.upload(file=media / "Cajun_instruments.jpg")
print(f"{myfile=}")

result = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[
        myfile,
        "\n\n",
        "Can you tell me about the instruments in this photo?",
    ],
)
print(f"{result.text=}")