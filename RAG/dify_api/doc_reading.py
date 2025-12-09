import requests
import os
import mimetypes
import yaml


cfg = yaml.safe_load(open("api_keys.yaml"))['doc_reading']


# --- Configuration ---
DIFY_API_KEY = cfg["api_key"]  # Your Dify API key
DIFY_API_BASE_URL = "https://api.dify.ai/v1" # e.g., "https://api.dify.ai/v1"
USER_ID = "abc-123"                 # A unique user identifier
PDF_PATH = "jd.pdf"          # Replace with the path to your local PDF file
QUERY_TEXT = "Where is the location mentioned in this document?" # Your text prompt


# ... [Configuration variables from above] ...

def upload_file_to_dify(file_path: str, api_key: str, base_url: str, user_id: str) -> str | None:
    """Uploads a local file (in this case, a PDF) to Dify and returns the file ID."""
    
    upload_url = f"{base_url}/files/upload"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    # MIME type should resolve to 'application/pdf'
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        print(f"⚠️ Could not determine MIME type for {file_path}. Defaulting to 'application/pdf'.")
        mime_type = 'application/pdf'

    try:
        with open(file_path, "rb") as f:
            files = {'file': (os.path.basename(file_path), f, mime_type)}
            data = {'user': user_id}

            print(f"⬆️ Uploading PDF from: {file_path}...")
            response = requests.post(upload_url, headers=headers, files=files, data=data)
            response.raise_for_status()

            result = response.json()
            file_id = result.get('id')
            
            if file_id:
                print(f"✅ PDF uploaded successfully. File ID: {file_id}")
                return file_id
            else:
                print(f"❌ PDF upload failed. Response: {result}")
                return None
    except requests.exceptions.RequestException as e:
        print(f"❌ An error occurred during file upload: {e}")
        return None
    except FileNotFoundError:
        print(f"❌ Error: File not found at path: {file_path}")
        return None
    

def send_multimodal_message(api_key: str, base_url: str, query: str, file_id: str, user_id: str):
    """Sends the text query and the PDF file ID to the chat API."""
    
    chat_url = f"{base_url}/chat-messages"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": {}, 
        "query": query,
        "files": [
            {
                # *** Change this from "image" to "file" ***
                "type": "document", 
                "transfer_method": "local_file",
                "upload_file_id": file_id
            }
        ],
        "response_mode": "blocking", 
        "user": user_id,
        "conversation_id": "" 
    }

    print(f"\n💬 Sending multimodal chat message: '{query}' with file ID: {file_id}...")
    try:
        response = requests.post(chat_url, headers=headers, json=payload)
        response.raise_for_status()

        chat_response = response.json()
        
        print("✅ Message sent successfully. Bot Answer:")
        print("---------------------------------------")
        print(chat_response.get("answer"))
        print("---------------------------------------")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ An error occurred during chat message send: {e}")
        if response is not None:
             print(f"Full Error Response: {response.text}")

# --- Main Execution ---
if __name__ == "__main__":
    # Note: You'll need to ensure 'my_report.pdf' exists or create a dummy PDF for testing.
    # The image creation logic from the previous example won't work for PDF.

    # Step 1: Upload the file
    uploaded_file_id = upload_file_to_dify(PDF_PATH, DIFY_API_KEY, DIFY_API_BASE_URL, USER_ID)

    if uploaded_file_id:
        # Step 2: Send the chat message with the file ID
        send_multimodal_message(DIFY_API_KEY, DIFY_API_BASE_URL, QUERY_TEXT, uploaded_file_id, USER_ID)
    else:
        print("\nProcess stopped because PDF upload failed.")