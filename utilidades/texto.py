import json

class Utils():
    def __init__(self):
        pass
    
    def save_text_in_file_based_time(self, content, tempo):
        file_name = tempo + ".json"
        try:
            # Convert dictionary to JSON string if content is a dictionary
            if isinstance(content, dict):
                content = json.dumps(content, indent=4)  # Pretty-print JSON
            # Write the content to the file
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(content)
            print(f"File saved as {file_name}")
        except Exception as ex:
            raise ValueError(f"Error saving content to file: {str(ex)}")

    def convert_text_to_markdown(self, generated_text: str, filename: str, tempo: str):
        try:
            # File path for the Markdown file
            markdown_file_path = f"{filename}_{tempo}.md"

            # Write the text content to the Markdown file
            with open(markdown_file_path, "w", encoding="utf-8") as md_file:
                md_file.write(generated_text)

            print(f"Markdown file saved as {markdown_file_path}")        
        except Exception as ex:
            raise ValueError(f"Erro ao converter o texto para markdown: {str(ex)}")