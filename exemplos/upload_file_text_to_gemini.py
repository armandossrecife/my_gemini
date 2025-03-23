from google import genai

client = genai.Client()
myfile = client.files.upload(file=media / "poem.txt")
print(f"{myfile=}")

result = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[myfile, "\n\n", "Can you add a few more lines to this poem?"],
)
print(f"{result.text=}")