import requests
import os
import mimetypes
import yaml


cfg = yaml.safe_load(open("api_keys.yaml"))['img']

# --- Configuration ---
DIFY_API_KEY = cfg["api_key"]  # Replace with your actual Dify API key
DIFY_API_BASE_URL = "https://api.dify.ai/v1" # e.g., "https://api.dify.ai/v1" or "http://localhost:5001/v1"
USER_ID = "abc-123"                 # A unique user identifier
IMAGE_PATH = "dog.jpg"         # Replace with the path to your local image file
QUERY_TEXT = "What is in this image?" # Your text prompt

# --- 1. Upload File Function ---
def upload_file_to_dify(file_path: str, api_key: str, base_url: str, user_id: str) -> str | None:
    """Uploads a local file to Dify and returns the file ID."""
    
    upload_url = f"{base_url}/files/upload"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    # Determine the MIME type of the file
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        print(f"⚠️ Could not determine MIME type for {file_path}. Defaulting to 'image/jpeg'.")
        mime_type = 'image/jpeg'

    # Dify expects a multipart/form-data request with specific fields
    try:
        with open(file_path, "rb") as f:
            # The 'files' dictionary is structured as:
            # {'form_field_name': ('filename', file_object, 'content_type')}
            files = {'file': (os.path.basename(file_path), f, mime_type)}
            
            # The 'data' dictionary holds non-file form fields
            data = {'user': user_id}

            print(f"⬆️ Uploading file from: {file_path}...")
            response = requests.post(upload_url, headers=headers, files=files, data=data)
            
            response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

            result = response.json()
            file_id = result.get('id')
            
            if file_id:
                print(f"✅ File uploaded successfully. File ID: {file_id}")
                return file_id
            else:
                print(f"❌ File upload failed. Response: {result}")
                return None
    except requests.exceptions.RequestException as e:
        print(f"❌ An error occurred during file upload: {e}")
        return None
    except FileNotFoundError:
        print(f"❌ Error: File not found at path: {file_path}")
        return None

# --- 2. Send Chat Message Function ---
def send_multimodal_message(api_key: str, base_url: str, query: str, file_id: str, user_id: str):
    """Sends the text query and the file ID to the chat API."""
    
    chat_url = f"{base_url}/chat-messages"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": {},  # Use this for pre-configured app inputs if needed
        "query": query,
        "files": [
            {
                "type": "image",
                "transfer_method": "local_file",
                "upload_file_id": file_id
            }
        ],
        "response_mode": "blocking", # Use "streaming" for real-time response chunks
        "user": user_id,
        "conversation_id": "" # Leave empty to start a new conversation
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
        
        # You might also want the conversation_id for follow-up messages
        conversation_id = chat_response.get("conversation_id")
        print(f"Conversation ID: {conversation_id}")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ An error occurred during chat message send: {e}")
        if response is not None:
             print(f"Full Error Response: {response.text}")

# --- Main Execution ---
if __name__ == "__main__":
    # Step 1: Upload the file
    uploaded_file_id = upload_file_to_dify(IMAGE_PATH, DIFY_API_KEY, DIFY_API_BASE_URL, USER_ID)

    if uploaded_file_id:
        # Step 2: Send the chat message with the file ID
        send_multimodal_message(DIFY_API_KEY, DIFY_API_BASE_URL, QUERY_TEXT, uploaded_file_id, USER_ID)
    else:
        print("\nProcess stopped because file upload failed.")