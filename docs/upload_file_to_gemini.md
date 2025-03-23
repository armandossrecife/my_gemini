```python
import requests
import os
import google.auth
from google.auth.transport.requests import AuthorizedSession

def upload_file_to_gemini(file_path, mime_type):
    """Uploads a file to Google Gemini using the upload URI."""

    upload_url = "https://generativelanguage.googleapis.com/upload/v1beta/files"

    try:
        # Get credentials using Google Auth
        credentials, project = google.auth.default()
        authed_session = AuthorizedSession(credentials)

        # Open the file in binary read mode
        with open(file_path, "rb") as file:
            file_data = file.read()

        # Prepare the request headers
        headers = {
            "Content-Type": mime_type,
        }

        # Make the POST request to upload the file
        response = authed_session.post(upload_url, headers=headers, data=file_data)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        # Parse the JSON response
        upload_response = response.json()
        return upload_response

    except requests.exceptions.RequestException as e:
        print(f"Error uploading file: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example Usage:
file_path = "your_file.pdf"  # Replace with the path to your file
mime_type = "application/pdf" #replace for the correct mime type

upload_result = upload_file_to_gemini(file_path, mime_type)

if upload_result:
    print("File uploaded successfully!")
    print(upload_result)
    # The response will contain the URI of the uploaded file, which you can use in subsequent requests.
    file_uri = upload_result.get("uri")
    if file_uri:
        print(f"File URI: {file_uri}")
    else:
        print("URI not found in the response.")
else:
    print("File upload failed.")

```

**Key improvements and explanations:**

1.  **Google Auth:**
    * The code now uses `google.auth.default()` to obtain credentials, which is the recommended approach for accessing Google Cloud APIs. This handles authentication more robustly.
    * `AuthorizedSession` is used to make authenticated requests.
2.  **Error Handling:**
    * Includes more comprehensive error handling using `try...except` blocks to catch `requests.exceptions.RequestException` (for network-related errors) and general `Exception` (for other unexpected errors).
    * `response.raise_for_status()` is now used to automatically raise an exception for HTTP error codes (4xx or 5xx), making it easier to detect and handle errors.
3.  **MIME Type:**
    * The code now requires you to specify the `mime_type` of the file being uploaded. This is crucial for the API to correctly process the file.
4.  **File Reading:**
    * The file is now read in binary mode (`"rb"`) to ensure that all file types are handled correctly.
5.  **Response Handling:**
    * The code now parses the JSON response from the API and extracts the `uri` of the uploaded file.
    * It also checks if the uri exists in the response, and informs the user if it does not.
6.  **Clearer Output:**
    * Provides more informative output messages to indicate whether the file upload was successful or failed.
    * Prints the file URI if available.
7.  **Dependencies:**
    * Requires the `requests` and `google-auth` libraries. You can install them with:
        ```bash
        pip install requests google-auth
        ```

**How to Use:**

1.  **Replace Placeholders:**
    * Replace `"your_file.pdf"` with the actual path to your file.
    * Replace `"application/pdf"` with the correct mime type of your file.
2.  **Run the Code:**
    * Execute the Python script.
3.  **Use the URI:**
    * If the upload is successful, the script will print the URI of the uploaded file. You can then use this URI in subsequent requests to the Gemini API (e.g., when providing media inputs to the model).

**Important Notes:**

* Ensure that you have the necessary permissions to access the Gemini API.
* The `google.auth.default()` function will automatically use your default Google Cloud credentials. If you need to use a different set of credentials, you can configure them using the `GOOGLE_APPLICATION_CREDENTIALS` environment variable.
* The mime type is very important, failing to provide the correct mime type will most likely result in a failed upload.